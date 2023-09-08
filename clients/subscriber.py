import paho.mqtt.client as mqtt

# Define the MQTT broker details
broker_address = "localhost"
broker_port = 1883

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")

# Create a MQTT client instance
client = mqtt.Client()

# Connect to the MQTT broker
try:
    client.connect(broker_address, broker_port)
    print("Broker is live")
except ConnectionRefusedError:
    print("No broker running on machine")
    exit(0)
# Set the message received callback
client.on_message = on_message

# Subscribe to a topic
# topic = "test/topic"
topic = "sensors/temeprature"
client.subscribe(topic)
# topic = "test/topic1"
topic = "sensors/humidity"
client.subscribe(topic)


# Start the MQTT loop to handle incoming messages
client.loop_start()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    # Disconnect from the MQTT broker on Ctrl+C
    client.disconnect()

