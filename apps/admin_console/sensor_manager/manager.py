import random
import time
from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit
from admin_console.config import CONFIG as config
from admin_console.config import CLIENT as client


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
    db = client[config["database_name"]]
    print(db.list_collection_names())

    input()
    pass


def ViewSensor():
    pass


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

    while choice != len(getMenuList()):
        WelcomeNote()

        for counter, option in enumerate(getMenuList()):
            print(f"{counter+1}.{option}")

        try:
            choice = int(input("Enter your choice:"))
        except:
            clearScreen()
            input("Enter the valid choice. Press enter  to continue")
            continue

        execute = Switch(choice)

        if execute is not None:
            execute()

        clearScreen()
