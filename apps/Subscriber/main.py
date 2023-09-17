import json
import sys
import threading
import time
import redis
import paho.mqtt.client as mqtt
from config import CONFIG as config
from config import CLIENT as mongo_client
from utility import clearScreen

# Global data : Start
client = None
redis_connection = None
redis_list = []
db = mongo_client[config["database_name"]]
topics = db["current_topics"]
sensors_data = db["sensor_data"]
RELOAD = None
RELOAD_CNT = 0
THREADCONTROL = None
# Global data : End


# Redis Publisher - Publishing Redis cache data
def RedisPublisher(redisChannel):
    # time.sleep(2)
    global THREADCONTROL
    global redis_list
    global redis_connection
    redis_channel = redisChannel

    fileName = "Redis_Published_Data.txt"
    #-------------------- Redis Data Publisher Code ------------------------------    
    
    try:
        while THREADCONTROL is None:

             # Initialize the list size to 0
            list_size = 0

            # Check the current size of the Redis list
            current_list_size = redis_connection.llen(redis_channel)

            # If the list size has increased, publish the new data
            if current_list_size > list_size:
            
                # Calculate the number of new items added
                num_new_items = current_list_size - list_size

                # Retrieve the new items from the list
                new_data = redis_connection.lrange(redis_channel, -num_new_items, -1)

                # Publish the new data to the Redis channel
                for item in new_data:
                    data = str(item)
                    redis_connection.publish(redis_channel, data)
                    with open(fileName, "a") as file:
                        file.write(f"{data}\n")

                # Update the list size
                list_size = current_list_size
    except Exception as e:
        print("Error in RedisPublisher...", e)

def on_disconnect(client, userdata, rc):
    clearScreen()
    global RELOAD
    RELOAD = 1
    # print("I am reloading...")
    # client.reconnect()

# MQTT Subscriber core code part 2
# Callback function when a MQTT message is received. Use this to populate Redis cache
def on_message(client, userdata, message):
    
    try:
        # print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
        
        if message.topic!= "publisher/status": # Only when publisher is publishing sensor readings. Else try reconnecting util manual exit.

            # Decode MQTT payload get message in Python <class = 'str'> format
            # message = message.payload.decode()

            # Make payload to JSON compatible format to get sensor data in format dictionary sent by sensors
            # message = message.replace("'", '"')
            # message = json.loads(message)

            # Publish decoded payload to Redis broker - populating Redis cache
            # redis_connection.set(message.topic, str(message))

            #------------------- Redis Server Caching Code ---------------------------------

            # Store the message in Redis list
            redis_connection.lpush(message.topic, message.payload.decode())

            # Keep only the latest 10 messages in the list
            redis_connection.ltrim(message.topic, 0, 9)


            # Retrieve data from Redis list
            # data_from_redis = []
            # redis_list_key = "sensors/humidity"
            
            # while True:
            #     item = redis_connection.rpop(redis_list_key)
            #     if item is None:
            #         break
            #     data_from_redis.append(item.decode())

            # # Insert data into MongoDB
            # if data_from_redis:
            #     # Create MongoDB documents and insert them into the collection
            #     documents = [{"data": item} for item in data_from_redis]
            #     sensors_data.insert_many(documents) 

        else: # Keep subscriber reconnecting, until publisher re-starts
            clearScreen()
            print(f"{message.topic}:{message.payload.decode()}")
            script_file = sys.argv[0]
            try:
                # Read the script's content
                with open(script_file, 'r') as file:
                    script_content = file.read()

                # Execute the script's content
                exec(script_content, globals())
            except Exception as e:
                print(f"Failed to reload the script: {e}")

    except redis.ConnectionError as e:
        clearScreen()
        print("Did not found any redis server.\nApplication terminating please wait...")
        client.disconnect()
        global RELOAD
        global THREADCONTROL
        THREADCONTROL = 1
        RELOAD = 1
        sys.exit(0)
    except Exception as e:
        print("Error in message processing...", e)
        
        return

def main():
    try:
        global THREADCONTROL
        try:
            # Load data from database
            topicList = []
            cursor = topics.find()
            for i in cursor:
                topicList.append(i["topic"])
            if len(topicList) !=0 :
                print("Listening on topics: ")
                for j in topicList:
                    print(j)
            else:
                print("No sensors in network")
                # print("Terminating application. Please wait...")
                # time.sleep(1)
                # exit(0)
            redisChannelList = list(set(topicList))
        except Exception as e:
            print("Unable to get topics....")

        #-------------------- Set MQTT --------------------------------

        # MQTT broker details
        broker_address = config["broker_address"]
        broker_port = config["broker_port"]

        # Create a MQTT client instance
        client = mqtt.Client()

        # Connect to the MQTT broker
        try:
            client.connect(broker_address, broker_port)
            print("Broker is live")
        except ConnectionRefusedError:
            print("No broker running on machine")
            sys.exit(0)

        # Subscribe to a topic
        for j in topicList:
            client.subscribe(j)

        # LWT setup
        # Subscribe to the LWT topic
        lwt_topic = "publisher/status"
        client.subscribe(lwt_topic)

        #------------------ Set Redis ----------------------------------

        # Redis connection details (these are default settings)
        redis_host = config["redis_address"]
        redis_port = config["redis_port"]
        redis_db = 0 #config["redis_db"][0]

        # Connect to a Redis server 
        try:
            global redis_connection
            redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db= redis_db)
            for i in redisChannelList:
                print(f"Redis Channel : {i}")
                thread_redis_pub = threading.Thread(target = RedisPublisher, args= [i])
                thread_redis_pub.start()
        except Exception as e:
            print("Did not found redis cache in system")
            sys.exit(0)


        #-------------- Subscriber core code part 1-------------------
        # Set the message received callback  
        client.on_message = on_message
        # Set callback when publishers disconnects
        client.on_disconnect = on_disconnect

        # Start the MQTT loop to handle incoming messages
        client.loop_start()    


        # Keep the script running. [Actually it should be running till topics are active.]
        global RELOAD
        while RELOAD is None:
            pass
       
    except ConnectionRefusedError:
        print("No broker running on machine.\nPlease wait, application terminating in 3 seconds...")
        THREADCONTROL = 1
        exit(0)
    except ValueError:
        print("No sensors running in the network. Application terminating please wait...")
        THREADCONTROL = 1
        client.loop_stop()
    except KeyboardInterrupt:
        # Disconnect from the MQTT broker on Ctrl+C
        THREADCONTROL = 1
        print("Client disconnected. Application is terminating please wait...")
        time.sleep(1)
        client.disconnect()

if __name__ == "__main__":
    main()

# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 -e REDIS_ARGS="--requirepass mypassword" redis/redis-stack:latest
# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# docker run -v redisinsight:/db -p 8001:8001 redislabs/redisinsight
