from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit


def getMenuList():
    return ["Add Sensor", "View Sensor", "Update Sensor", "Delete Sensor", "Restart Sensor", "Turnoff Sensor", "Exit"]


def Switch(choice):
    action = {
        1: AddSensor,
        2: ViewSensor,
        3: UpdateSensor,
        4: DeleteSensor,
        5: RestartSensor,
        6: TurnOffSensor,
        7: Exit
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
