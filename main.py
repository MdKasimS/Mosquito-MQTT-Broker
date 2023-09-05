import sys
from time import sleep
import broker
from utility import clearScreen
from utility import Exit
from utility import WelcomeNote
from config import configuration as config

# Global configuration
MOSPID = None


def getMenuList():
    return ["Restart Broker", "Exit"]


def Switch(choice):
    action = {
        1: RestartBroker,
        2: Exit
    }

    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")


def RestartBroker():

    print("Restarting broker....")
    sleep(1)

    # Kill the existing broker
    broker.closeBroker(MOSPID)
    clearScreen()

    # Reloading code which restarts the broker
    script_file = sys.argv[0]
    try:
        # Read the script's content
        with open(script_file, 'r') as file:
            script_content = file.read()

        # Execute the script's content
        exec(script_content, globals())
    except Exception as e:
        print(f"Failed to reload the script: {e}")

    # reloadScript(script_file) This is not working


def Terminate():
    if MOSPID is not None:
        broker.closeBroker(MOSPID)
        exit(0)
    else:
        print(f'Process {config["process_name"]} not found.')


def main():
    clearScreen()
    broker.initBroker(config["start"])

    global MOSPID
    # Actual PID using psutil
    MOSPID = broker.get_pid_by_name(config["process_name"])
    while 1:
        WelcomeNote()

        print("< Note: Use Admin Console For Network Management >")
        for counter, option in enumerate(getMenuList()):
            print(f"{counter+1}. {option}")

        try:
            choice = int(input("Enter your choice:"))
        except:
            clearScreen()
            input("Enter the valid choice. Press enter to continue")
            continue
        execute = Switch(choice)

        if execute is not None:
            if choice != len(getMenuList()):
                execute()
            else:
                execute([Terminate, print, input])
        clearScreen()


if __name__ == "__main__":
    main()
