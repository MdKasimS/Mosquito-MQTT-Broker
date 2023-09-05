import random
import time
from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit
from .config import CONFIG as config
from .config import CLIENT as client
from pymongo import DESCENDING

db = client[config["database_name"]]
collection = db["sensors"]


def getMenuList():
    return ["Add Sensor", "View Sensor", "Update Sensor", "Delete Sensor", "Restart Sensor", "Turnoff Sensor", "Exit"]

def Switch(choice):
    action = {
        1: AddSensor,    # all sensors
        2: ViewSensor,   # active sensors
        3: UpdateSensor,  # all sensors
        4: DeleteSensor,  # all sensors
        5: RestartSensor,  # all sensors & active sensors
        6: TurnOnSensor,  # all sensors
        7: TurnOffSensor,  # active sensors
        8: Exit
    }
    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")

def AddSensor():
    
    last_record = collection.find_one({}, sort=[('sensor_id',DESCENDING)])

    nextId = last_record["sensor_id"] + 1
   
    try:
        collection.insert_one({
            "sensor_id": nextId,
            "type": "default",
            "topic": "test/topic",
            "publisher": True,
            "subscriber": False,
            "default": 35,
            "status": True
        })
    except Exception as e:
        clearScreen()
        key = 0
        value = 0
        input(f"Sensors can't be of same details -> {key}:{value}\nPress enter to continue...")
        return

    clearScreen()
    input("Sensor Has Been Successfully Added!\nPress Enter To Continue")
    # clearScreen()

def ViewSensor():
    clearScreen()
    last_record = collection.find_one({}, sort=[('sensor_id',DESCENDING)])
    
    for key,value in last_record.items():
        print(key, ": ", value)
    input("\nPress Enter To Continue...")

def UpdateSensor():
    pass

def RestartSensor():
    pass

def DeleteSensor():
    pass

def TurnOnSensor():
    pass

def TurnOffSensor():
    pass

def simulate_sensor(sensor_id):
    while True:
        # Simulate sensor data
        sensor_data = 35 + random.randint(0, 100)/100 % 30

        # Generate a unique filename for each sensor
        filename = f"sensor_{sensor_id}.txt"

        # Write data to the text file
        with open(filename, "a") as file:
            file.write(f"Sensor-{sensor_id} Data: {sensor_data}\n")

        # Sleep for a while before the next reading
        time.sleep(1)

def getActiveSensors():
    return []  # active sensor list from database

def filter(criteria):
    pass

def Menu():
    clearScreen()
    choice = ""
    # Database()
    if client.server_info():
        while choice != len(getMenuList()):
            WelcomeNote()

            for counter, option in enumerate(getMenuList()):
                print(f"{counter+1}.{option}")

            try:
                choice = int(input("Enter your choice:"))
            except:
                clearScreen()
                input("Enter the valid choice. Press enter  to  continue")
                continue

            execute = Switch(choice)

            if execute is not None:
                execute()

    else:
        clearScreen()
        input("Server Disconnected. Please Press Enter To Continue..")
        return
