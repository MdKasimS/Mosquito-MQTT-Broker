from time import sleep
import paho.mqtt.client as mqtt

# Define the MQTT broker details
broker_address = "localhost"
broker_port = 1883

# Create a MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Publish a message to a topic
topic = "test/topic"
message = "25.1"
# client.publish(topic, message)

try:
    while True:
        client.publish(topic, message)
        message = (float(message) + 0.1) % 5
        sleep(10)
        
except KeyboardInterrupt:
    # Disconnect from the MQTT broker
    client.disconnect()
