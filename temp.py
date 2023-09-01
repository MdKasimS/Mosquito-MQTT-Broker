import os
import sys

def restart_script():
    script_file = sys.argv[0]

    try:
        # Read the script's content
        with open(script_file, 'r') as file:
            script_content = file.read()

        # Execute the script's content
        exec(script_content, globals())
    except Exception as e:
        print(f"Failed to reload the script: {e}")


# Call the restart_script function to restart the script
restart_script()


print("I am python script")
input("Should I reload?")

