import json
import sys
import time
import redis
import paho.mqtt.client as mqtt
from config import CONFIG as config
from config import CLIENT as mongo_client
from utility import clearScreen

# Global data : Start
client = None
redis_connection = None
db = mongo_client[config["database_name"]]
topics = db["current_topics"]
RELOAD = None
# Global data : End


# Redis cache implementation to handle messages
def StartRedis():

    pass

# def reloadScript():
def on_disconnect(client, userdata, rc):
    clearScreen()
    global RELOAD
    RELOAD = 1
    print("I am reloading...")
    client.reconnect()

# Callback function when a MQTT message is received. Use this to populate Redis cache
def on_message(client, userdata, message):
    
    try:
        print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
        
        if message.topic!= "publisher/status": # Only when publisher is publishing sensor readings. Else try reconnecting util manual exit.

            # Decode MQTT payload get message in Python <class = 'str'> format
            message = message.payload.decode()

            # Make payload to JSON compatible format to get sensor data in format dictionary sent by sensors
            message = message.replace("'", '"')
            message = json.loads(message)

            # Publish decoded payload to Redis broker - populating Redis cache
            redis_connection.set(message["sensor_id"], str(message))
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
    except Exception as e:
        print("Error in message processing...")
        return

def main():
    try:
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
        except Exception as e:
            print("Unable to get topics....")

        #-------------------- Set MQTT --------------------------------

        # MQTT broker details
        broker_address = "localhost"
        broker_port = 1883

        # Create a MQTT client instance
        client = mqtt.Client()

        # Connect to the MQTT broker
        try:
            client.connect(broker_address, broker_port)
            print("Broker is live")
        except ConnectionRefusedError:
            print("No broker running on machine")
            exit(0)

        # Subscribe to a topic
        for j in topicList:
            client.subscribe(j)

        # LWT setup
        # Subscribe to the LWT topic
        lwt_topic = "publisher/status"
        client.subscribe(lwt_topic)



        #------------------ Set Redis ----------------------------------
        # Redis connection details (these are default settings)
        redis_host = "localhost"
        redis_port = 6379
        redis_db = 0

        # Connect to a Redis server 
        try:
            global redis_connection
            redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db= redis_db)
        except Exception as e:
            print("No redis cache on machine")
            exit(0)



        # for i in sensor_data.keys():
        #     # Retrieve a value by key
        #     value = redis_connection.get(i)
        #     print(value.decode())  # Decode bytes to a string

        # Set callback when publishers diconnects
        client.on_disconnect = on_disconnect
        # Set the message received callback
        client.on_message = on_message

        # Start the MQTT loop to handle incoming messages
        client.loop_start()    



        # Keep the script running. [Actually it should be running till topics are active.]
        global RELOAD
        while True : #RELOAD is None:
            pass
        # else:
        #     print("Reload has bee changed")
        #     RELOAD = None
        #     script_file = sys.argv[0]
        #     try:
        #         # Read the script's content
        #         with open(script_file, 'r') as file:
        #             script_content = file.read()

        #         # Execute the script's content
        #         exec(script_content, globals())
        #     except Exception as e:
        #         print(f"Failed to reload the script: {e}")

    except ConnectionRefusedError:
        print("No broker running on machine.\nPlease wait, application terminating in 3 seconds...")
        exit(0)
    except ValueError:
        print("No sensors running in the network. Application terminating please wait...")
        client.loop_stop()
    except KeyboardInterrupt:
        # Disconnect from the MQTT broker on Ctrl+C
        print("Client disconnected. Application is terminating please wait...")
        time.sleep(1)
        client.disconnect()

if __name__ == "__main__":
    main()

