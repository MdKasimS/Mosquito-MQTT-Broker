import random
import threading
import time
import paho.mqtt.client as mqtt


from sensor_manager import manager as sensor
from subscriber_manager import manager as subscriber
from broker_manager import manager as broker

from utility import clearScreen
from utility import Exit
from utility import WelcomeNote
from utility import CONFIGURATION as config
from config import CLIENT as client
from database import data 

# Global data
THREADCONTROL = None

db = client["iot_data"]
collection = db["sensors"]

pubPool = data.PUBTHREADPOOL
subPool = data.SUBTHREADPOOL
active_sensors = data.ACTIVE_SENSORS
active_subscriber = data.ACTIVE_SUBSCRIBERS

def simulate_sensor(sensor):

    # Define the MQTT broker details
    broker_address = config["broker_address"] #"localhost"
    broker_port = config["broker_port"] #1883

    # Create a MQTT client instance
    client = mqtt.Client()

    # Connect to the MQTT broker
    client.connect(broker_address, broker_port)

    # Publish a message to a topic
    topic = sensor["topic"]
    

    while THREADCONTROL is None:

        # Simulate sensor data
        sensor_data = sensor["default"] + round(random.randint(0, 100)/100 % 30, 3)

        # Generate a unique filename for each sensor
        filename = f"sensor_{sensor['sensor_id']}.txt"

        #publish data
        try:
            client.publish(topic, sensor_data)
        except Exception as e:
            client.disconnect()

        # Write data to the text file
        with open(filename, "a") as file:
            file.write(f"Sensor-{sensor['sensor_id']} Data: {sensor_data}\n")

            # Sleep for a while before the next reading
            time.sleep(1)



def getMenuList():
    return ["Manage Sensors", "Manage Subscribers", "Manage Topics", "Exit"]


def Switch(choice):
    action = {
        1: ManageSensor,
        2: ManageSubscriber,
        3: ManageTopic,
        4: Exit
    }
    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")


def ManageSensor():
    sensor.Menu()


def ManageSubscriber():
    subscriber.Menu()


def ManageTopic():
    broker.Menu()


def main():
    clearScreen()

    while True:

        WelcomeNote()

        # Load database data
        cursor = collection.find()

        for document in cursor:
            if document["status"] == True:
                active_sensors.append(document)


        # Start default sensors with default values-Threads
        # Create and start multiple threads for simulating sensors
        for i in active_sensors:
            thread = threading.Thread(target=simulate_sensor, args=(i,))
            pubPool.append(thread)
            thread.start()
        
        # Start default subscribers with default values-Threads


        # Menu
        for counter, option in enumerate(getMenuList()):
            print(f"{counter+1}.{option}")

        try:
            choice = int(input("Enter your choice:"))
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
