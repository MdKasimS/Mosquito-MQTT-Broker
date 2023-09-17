import json
import time
import redis
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from config import CONFIG as config

# Global data : Start
client = None
redis_connection = None
redis_list = []
mongo = MongoClient(config["database_address"])
db = mongo[config["database_name"]]
topics = db["current_topics"]

# Global data : End


# Callback function when a MQTT message is received. Use this to populate Redis cache
def on_message(client, userdata, message):
    global redis_list
    redis_channel = "humidity_channel"
    try:
        
        print(f"Received message on topic '{message.topic}': {message.payload.decode()}")

        # Store the message in Redis list
        redis_connection.lpush(message.topic, message.payload.decode())

        # Keep only the latest 10 messages in the list
        redis_connection.ltrim(message.topic, 0, 9)

        # Initialize the list size to 0
        list_size = 0

        while True:
            # Check the current size of the Redis list
            current_list_size = redis_connection.llen(redis_list)

            # If the list size has increased, publish the new data
            if current_list_size > list_size:
                # Calculate the number of new items added
                num_new_items = current_list_size - list_size

                # Retrieve the new items from the list
                new_data = redis_connection.lrange(redis_list, -num_new_items, -1)

                # Publish the new data to the Redis channel
                for item in new_data:
                    redis_connection.publish(redis_channel, item)

                # Update the list size
                list_size = current_list_size



            # ---------------- Testing Arrangement Start ------------------------------
            # Decode MQTT payload get message in Python <class = 'str'> format
            topic = message.topic
            message = message.payload.decode()
            message = message.replace("'", '"')
            message = json.loads(message)

            # Write data to the text file [FOR TESTING]
            with open("subscriber_786.csv", "a") as file:
                print(f"{message['sensor_id']} : {message['value']} : {message['timestamp']}\n")
                file.write(f"{message['sensor_id']},{message['value']},{message['timestamp']}\n")

            # Publish decoded payload to Redis broker - populating Redis cache
            redis_connection.set(message["sensor_id"], str(message))

            # ---------------- Testing Arrangement End ------------------------------

            # Sleep for a short interval before checking again
            time.sleep(1)

    except Exception as e:
        print("Error in message processing...", e)
        return
    
def main():

    # Load data from database
    topicList = []
    cursor = topics.find()
    try:
        for i in cursor:
            topicList.append(i["topic"])
        if len(topicList) !=0 :
            print("Listening on topics: ")
            for j in topicList:
                print(j)
        else:
            print("No sensors in network")
            print("Terminating applicatioin. Please wait...")
            time.sleep(2)
            exit(0)
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



    #------------------ Set Redis ----------------------------------
    # Redis connection details (these are default settings)
    redis_host = "localhost"
    redis_port = 6379
    redis_db = 0

    redis_list = 'sensors/humidity'
    redis_channel = 'humidity_channel'

    # Initialize the list size to 0
    list_size = 0


    # Connect to a Redis server 
    try:
        global redis_connection
        redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db= redis_db)
    except Exception as e:
        print("No redis cache on machine")
        exit(0)

     # Set the message received callback
    client.on_message = on_message

    # Start the MQTT loop to handle incoming messages
    client.loop_start()

    # Keep the script running
    try:
        while True:
            pass
    except KeyboardInterrupt:
        # Disconnect from the MQTT broker on Ctrl+C
        client.disconnect()

if __name__ == "__main__":
    main()