import os
import sys


def WelcomeNote():
    clearScreen()
    # print(" "*5 + "|| Exalens IoT Networks ||")
    print(" " * 7 + "Network Admin Console")
    # print("----------------------------------")
    print("_________<Manage Sensors>_________")


def clearScreen():
    try:
        # Determine the operating system
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-like (Linux, macOS)
            os.system('clear')
    except Exception as e:
        print(f"Failed to clear the console: {e}")


def Exit():
    return


def reloadScript(script_file):
    try:
        # Read the script's content
        with open(script_file, 'r') as file:
            script_content = file.read()

        # Execute the script's content
        exec(script_content, globals())
    except Exception as e:
        print(f"Failed to reload the script: {e}")
