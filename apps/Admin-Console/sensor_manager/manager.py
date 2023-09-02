from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit


def getMenuList():
    return ["Add Sensor", "View Sensor", "Update Sensor", "Delete Sensor", "Restart Sensor", "Turnoff Sensor", "Exit"]


def Switch(choice):
    action = {
        1: AddSensor,    # all sensors
        2: ViewSensor,   # active sensors
        3: UpdateSensor,  # all sensors
        4: DeleteSensor,  # all sensors
        5: RestartSensor,  # all sensors
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
