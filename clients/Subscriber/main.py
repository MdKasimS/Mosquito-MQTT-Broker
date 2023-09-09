import time
import paho.mqtt.client as mqtt
from config import CONFIG as config
from config import CLIENT as client
from utility import WelcomeNote

# Global data : Start
db = client[config["database_name"]]
topics = db["current_topics"]

topicList = []
# Global data : End


# Redis cache implementation to handle messages
def StartRedis():

    pass



# Callback function when a message is received
def on_message(client, userdata, message):
    
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")
    # print(f"Received message on topic '{message.topic}': {message}")

def main():
    try:
        # Define the MQTT broker details
        broker_address = config["broker_address"]
        broker_port = config["broker_port"]

        # Create a MQTT client instance
        client = mqtt.Client()

        # Connect to the MQTT broker
        client.connect(broker_address, broker_port)
        WelcomeNote()        

        # Set the message received callback
        client.on_message = on_message


        # Load database-topics data
        cursor = topics.find()
        topicList = []
        for i in cursor:
            topicList.append(i['topic'])
        
        # Check active sensors in network
        if not topicList:
            raise ValueError("The list is empty. Cannot proceed with the operation.")
        else:
            for i in topicList:
                client.subscribe(i)

        # Start the MQTT loop to handle incoming        messages
        client.loop_start()

        # Keep the script running. [Actually it should be running till topics are active.]
        while True:
            pass

    except ConnectionRefusedError:
        print("No broker running on machine.\nPlease wait, application terminating in 3 seconds...")
        exit(0)
    except ValueError:
        print("No sensors running in the network. Application terminating please wait...")
        client.loop_stop() 
    except KeyboardInterrupt:
        # Disconnect from the MQTT broker on Ctrl+C
        time.sleep(1)
        print("Client disconnected. Press enter to quit application.")
        client.disconnect()

if __name__ == "__main__":
    main()

