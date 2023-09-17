import queue
import random
import sys
import threading
import time
import redis
import datetime
import paho.mqtt.client as mqtt


from sensor_manager import manager as sensor
from subscriber_manager import manager as subscriber
# from broker_manager import manager as broker

from utility import clearScreen
from utility import Exit
from utility import WelcomeNote
from config import CLIENT as client, SETTING as setting, CONFIG as config
from database import data 

# Global data : Start
THREADCONTROL = None

redis_connection = None

db = client[config["database_name"]] #"iot_data"
sensors = db[config["collection_list"][0]]
subscribers = db[config["collection_list"][1]]
topics = db[config["collection_list"][5]]
sensors_data = db[config["collection_list"][2]]

pubPool = data.PUBTHREADPOOL
subPool = data.SUBTHREADPOOL
active_sensors = data.ACTIVE_SENSORS
active_subscribers = data.ACTIVE_SUBSCRIBERS
active_topics = data.ACTIVE_TOPICS
# Global data : End 

def simulate_sensor(thread,sensor):       
    # Define the MQTT broker details
    broker_address = setting["broker_address"] 
    broker_port = setting["broker_port"] 

    # Last Will and Testament (LWT) configuration
    lwt_topic = "publisher/status"
    lwt_message = "Publisher disconnected"

    # Create a MQTT client instance
    client = mqtt.Client()

    # Set the LWT message
    client.will_set(lwt_topic, lwt_message, qos=1, retain=True)

    # Connect to the MQTT broker
    try:
        client.connect(broker_address, broker_port)
    except Exception as e:
        print("No Broker Found Running...")
        return

    try:
        # Update Topics
        topic = {
            "sensor_id" : sensor["sensor_id"],
    		"topic" : sensor["topic"],
    		"threadId" : pubPool[thread].ident, #thread.ident,
    		"timestamp" : datetime.datetime.now().isoformat()
        }
        topics.insert_one(topic)
    except Exception as e:
        input("CHeck error....")

     # Generate a unique filename for each sensor
    filename = f"sensor_{sensor['sensor_id']}.txt"
    
    # Publish a message to a topic
    topic = sensor["topic"]
    
    while THREADCONTROL is None:

        # Simulate sensor data
        sensor_value = sensor["default"] + (random.randint(0, 100) % 50)/100
        sensor_value = round(sensor_value, 3)

        # Prepare payload
        sensor_data = { 
            "sensor_id" : sensor["sensor_id"],
            "value" : sensor_value,
            "timestamp" : datetime.datetime.now().isoformat()
        }


        # Publish data in string formatted only
        try:
            client.publish(topic, str(sensor_data))
        except Exception as e:
            StopAllClients()
            client.disconnect()
            print("Error Occured In Broker")
            input(e)
       
        
        # Write data to the text file [FOR TESTING]
        with open(filename, "a") as file:
            # file.write(f"Sensor-{sensor['sensor_id']} Data: {sensor_data}\n")
            file.write(f"{sensor_data}\n")

            # Sleep for a while before the next reading
            time.sleep(1)

def subscribe(thread, mqtt_subscriber):

    # Callback function when a message is received
    def on_message(client, userdata, message): # Not accessible outside subscribe() function.
        # Write data to the text file [FOR TESTING]
        with open(filename, "a") as file:
            file.write(f"{message.topic} : {message.payload.decode()}\n")

            # Sleep for a while before the next reading
            # time.sleep(1)
    
    # Define the MQTT broker details. <<<Modification: Needs Redis Subscriber>>>
    broker_address = setting["broker_address"] 
    broker_port = setting["broker_port"] 

    # Create a MQTT client instance
    client = mqtt.Client()

    # Connect to the MQTT broker
    try:
        client.connect(broker_address, broker_port)
    except Exception as e:
        print("No Broker Found Running...")
        return

    # Set the message received callback
    client.on_message = on_message

    # Generate a unique filename for each sensor
    filename = f"subscriber_{mqtt_subscriber['subscriber_id']}.txt"
    
    # Publish a message to a topic
    topic = mqtt_subscriber["topic"]
    client.subscribe(topic)

    client.loop_start()

    while THREADCONTROL is None:
            # time.sleep(1)
        pass

def connectRedis():
    global redis_connection
    redis_host = config["redis_address"]
    redis_port = config["redis_port"]
    redis_db = config["redis_db"][0]
    print(f"Redis host : {redis_host}\nRedis port : {redis_port}\nRedis db : {redis_db}")

    # Connect to a Redis server 
    try:
        global redis_connection
        redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db= redis_db)
    except Exception as e:
        print("Did not found redis cache in system")
        sys.exit(0)
    
def getMenuList():
    return ["Manage Sensors", "Manage Subscribers", "Manage Topics", "Re-Start All Clients","Stop All Clients","Exit"]

def Switch(choice):
    action = {
        1: ManageSensor,
        2: ManageSubscriber,
        3: ManageTopic,
        4: RestartClients,
        5: StopAllClients,
        6: Exit
    }
    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")

def ManageSensor():
    sensor.Menu()

def ManageSubscriber():
    subscriber.Menu(client)

def ManageTopic():
    pass
    # broker.Menu(client)

def StartClients(active_clients):
    global THREADCONTROL
    THREADCONTROL = None
    # Create and start multiple threads for simulating sensors.
    for counter, mqtt_client in enumerate(active_clients):
        if mqtt_client["publisher"] == True: 
            thread = threading.Thread(target=simulate_sensor, args=(counter, mqtt_client))
            pubPool.append(thread)
        else:
            thread = threading.Thread(target=subscribe, args=(counter, mqtt_client))
            subPool.append(thread)
            input("This is subscriber")
        
        thread.start()

def StartRedis(redisChannels):
    
    try:
        for i in redisChannels:
            print(i)
            thread = threading.Thread(target=RedisToDb, args=[i])
            thread.start()
    except Exception as e:
        input(f"Error in starting redis..., {e}")
        sys.exit(0)


#----------------- Redis Subscriber Code ----------------------
def RedisToDb(redisChannel):

    # Subscribe to the Redis channel
    pubsub = redis_connection.pubsub()
    pubsub.subscribe(redisChannel)
    
    fileName = f"sensor_data.txt"

    try:
        while THREADCONTROL is None:
        
            # Listen for messages on the Redis channel
            for message in pubsub.listen():
                
                if message['type'] == 'message':

                    # Decode the message from bytes to string
                    data = message['data'].decode('utf-8')
                    # print(f"Received message: {data}")

                    with open(fileName, "a") as file:
                        file.write(f"{data}\n")

                    # Insert the data into the MongoDB collection
                    # sensors_data.insert_one({"message": data})

    except Exception as e:
        print("Error in RedisToDb....", e)


def StopAllClients():
    global THREADCONTROL
    global topics
    THREADCONTROL = 1
    topics.delete_many({})

    clearScreen()
    input("All clients have been stopped successfully. Press enter to continue...")

def RestartClients():
    
    StopAllClients()
    StartClients(active_sensors)

    StartRedis()

    # StartClients(active_subscribers)

    clearScreen()
    input("All clients have been restarted. Press enter to continue...")

def main(): 

    clearScreen()

    # Load database-sensors data
    cursor = sensors.find()
    for mqtt_client in cursor:
        if mqtt_client["status"] == True:
            active_sensors.append(mqtt_client)

     # Start default sensors with default values-Threads.
    StartClients(active_sensors)

    # Load database-topics data
    cursor = topics.find()
    topicList = []
    for i in cursor:
        topicList.append(i['topic'])

    # Start redis
    connectRedis()
    StartRedis(list(set(topicList))) 

    #-------------- Arrangement For Testing ------------------------------
    # Load database-subscribers data
    # cursor = subscribers.find()
    # for mqtt_client in cursor:
    #     if mqtt_client["status"] == True and mqtt_client["topic"] in topicList: # And if its topic is in topic collection
    #         active_subscribers.append(mqtt_client)
    #         # input("We got a subscriber...")
    
    time.sleep(2)   
    # Start default subscribers with default values-Threads
    # StartClients(active_subscribers)        
    #----------------------------------------------------------------------

    while True:

        WelcomeNote()

        # Menu
        for counter, option in enumerate(getMenuList()):
            print(f"{counter+1}.{option}")

        try:
            choice = int(input("Enter your choice: "))
            if choice == len(getMenuList()):
                StopAllClients()
        except Exception as e:
            clearScreen()
            input("Enter the valid choice. Press enter  to continue")
            continue
        except KeyboardInterrupt:
            # Disconnect from the MQTT broker on Ctrl+C
            # client.close()
            global THREADCONTROL
            THREADCONTROL = 1
            clearScreen()
            print("System terminating. Please wait...")
            time.sleep(2)
            exit(0)

        execute = Switch(choice)

        try:
            if execute is not None:
                execute()
        except Exception as e:
            # client
            THREADCONTROL = 1
        clearScreen()

if __name__ == "__main__":
    main()
