from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit

def getMenuList():
    return ["Add Subscriber", "View Subscriber", "Update Subscriber", "Delete Subscriber", "Restart Subscriber", "Exit"]


def Switch(choice):
    action = {
        1: AddSubscriber,
        2: ViewSubscriber,
        3: UpdateSubscriber,
        4: DeleteSubscriber,
        5: RestartSubscriber,
        6: TurnOnSubscriber,
        7: TurnOffSubscriber,
        8: Exit
    }
    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")


def AddSubscriber():
    pass


def ViewSubscriber():
    pass


def UpdateSubscriber():
    pass


def RestartSubscriber():
    pass


def DeleteSubscriber():
    pass


def TurnOnSubscriber():
    pass


def TurnOffSubscriber():
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
