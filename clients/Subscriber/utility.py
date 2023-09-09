import os

def WelcomeNote():
    print("Broker Is Live")


def clearScreen():
    try:
        # Determine the operating system
        if os.name == 'nt':  # Windows
            os.system('cls')
        else:  # Unix-like (Linux, macOS)
            os.system('clear')
    except Exception as e:
        print(f"Failed to clear the console: {e}")
