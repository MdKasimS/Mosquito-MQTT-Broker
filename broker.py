import subprocess


def initBroker(server):
    # Start the Mosquitto broker using  subprocess
    try:
        subprocess.run([server],   check=True)
    except subprocess.  CalledProcessError:
        print("An error occurred while  starting the Mosquitto MQTT  server.")
    return 0
