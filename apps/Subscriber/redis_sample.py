import json
import time
import redis
import paho.mqtt.client as mqtt
from pymongo import MongoClient
from config import configuration as config


# Callback function when a MQTT message is received. Use this to populate Redis cache
def on_message(client, userdata, message):
    
    try:
        # print(f"Received message on topic '{message.topic}': {message.payload.decode()}")

        # Decode MQTT payload get message in Python <class = 'str'> format
        message = message.payload.decode()
        # Make payload to JSON compatible format to get sensor data in format dictionary sent bysensors
        message = message.replace("'", '"')
        message = json.loads(message)
        print(message)
        
    except Exception as e:
        print("Error in message processing...")
        return


# Global data : Start
client = None
redis_connection = None
mongo = MongoClient(config["database_address"])
db = mongo[config["database_name"]]
topics = db["current_topics"]

# Global data : End

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

# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 -e REDIS_ARGS="--requirepass mypassword" redis/redis-stack:latest
# docker run -d --name redis-stack -p 6379:6379 -p 8001:8001 redis/redis-stack:latest
# docker run -v redisinsight:/db -p 8001:8001 redislabs/redisinsight
