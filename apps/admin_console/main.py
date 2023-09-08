import queue
import random
import threading
import time
import datetime
import paho.mqtt.client as mqtt


from sensor_manager import manager as sensor
from subscriber_manager import manager as subscriber
from broker_manager import manager as broker

from utility import clearScreen
from utility import Exit
from utility import WelcomeNote
from config import CLIENT as client, SETTING as setting, CONFIG as config
from database import data 

# Global data : Start
THREADCONTROL = None

db = client[config["database_name"]] #"iot_data"
sensors = db[config["collection_list"][0]]
subscribers = db[config["collection_list"][1]]
topics = db[config["collection_list"][5]]

pubPool = data.PUBTHREADPOOL
subPool = data.SUBTHREADPOOL
active_sensors = data.ACTIVE_SENSORS
active_subscribers = data.ACTIVE_SUBSCRIBERS

# Global data : End 

def simulate_sensor(thread,sensor):

    print(f"Thread starting.... for {sensor}")
    
    # Update Topics
    topic = {
        "sensor_id" : sensor["sensor_id"],
		"topic" : sensor["topic"],
		"threadId" : thread, #thread.ident,
		"timestamp" : datetime.datetime.now().isoformat()
    }

    topics.insert_one(topic)
         
    # Define the MQTT broker details
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

    # Publish a message to a topic
    topic = sensor["topic"]
    
    while THREADCONTROL is None:

        # Simulate sensor data
        sensor_value = sensor["default"] + (random.randint(0, 100) % 50)/100
        sensor_value = round(sensor_value, 3)

        # Generate a unique filename for each sensor
        filename = f"sensor_{sensor['sensor_id']}.txt"

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
            client.disconnect()
        
        # Write data to the text file [FOR TESTING]
        with open(filename, "a") as file:
            # file.write(f"Sensor-{sensor['sensor_id']} Data: {sensor_data}\n")
            file.write(f"{sensor_data}\n")

            # Sleep for a while before the next reading
            time.sleep(1)


def redis():

    redis_queue = queue.Queue()

    while THREADCONTROL is None:

        #subscriber code

        #publisher code

        
        pass


def getMenuList():
    return ["Manage Sensors", "Manage Subscribers", "Manage Topics", "Re-Start All Clients","Exit"]


def Switch(choice):
    action = {
        1: ManageSensor,
        2: ManageSubscriber,
        3: ManageTopic,
        4: RestartClients,
        5: Exit
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
    broker.Menu()

def StartThreads(active_clients):

    # Create and start multiple threads for simulating sensors.
    for counter, mqtt_client in enumerate(active_clients):
        # input(f"{mqtt_client} {counter}")
        thread = threading.Thread(target=simulate_sensor, args=(counter, mqtt_client))
        if mqtt_client["publisher"] == True: 
            pubPool.append(thread)
            # input("This is publisher")
        else:
            subPool.append(thread)
            # input("This is subscriber")

        thread.start()

def StartRedis():
    thread = threading.Thread(target=redis)
    thread.start()

    # input(type(pubPool[0]))
    # for i in pubPool:
    #     input(i)


def RestartClients():

    global active_sensors
    StartThreads(active_sensors)
    # StartRedis()
    # StartThreads(active_subscribers)


def main():
    clearScreen()

    # Load database-sensors data
    cursor = sensors.find()
    for document in cursor:
        if document["status"] == True:
            active_sensors.append(document)

    # Load database-subscribers data
    cursor = subscribers.find()
    for document in cursor:
        if document["status"] == True: # And if its topic is in topic collection
            active_subscribers.append(document)

    # Start default sensors with default values-Threads.
    StartThreads(active_sensors)

    # Start redis
    # StartRedis()        

    # Start default subscribers with default values-Threads        

    while True:

        WelcomeNote()

        # Menu
        for counter, option in enumerate(getMenuList()):
            print(f"{counter+1}.{option}")

        try:
            choice = int(input("Enter your choice: "))
            if choice == len(getMenuList()):
                global THREADCONTROL
                THREADCONTROL= 1 
        except Exception as e:
            clearScreen()
            input("Enter the valid choice. Press enter  to continue")
            continue
        
        execute = Switch(choice)

        try:
            if execute is not None:
                execute()
        except Exception as e:
            client
        clearScreen()


if __name__ == "__main__":
    main()
