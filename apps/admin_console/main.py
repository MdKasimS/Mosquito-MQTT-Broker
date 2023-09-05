from sensor_manager import manager as sensor
from subscriber_manager import manager as subscriber
from broker_manager import manager as broker

from utility import clearScreen
from utility import Exit
from utility import WelcomeNote


from utility import CONFIG as config


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

    while 1:

        WelcomeNote()

        # Get database configured

        # Start default sensors with default values-Threads

        # Start default subscribers with default values-Threads

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


if __name__ == "__main__":
    main()
