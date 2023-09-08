import paho.mqtt.client as mqtt
import redis

# MQTT broker details
broker_address = "localhost"
broker_port = 1883

# Redis connection details
redis_host = "localhost"
redis_port = 6379
redis_db = 0

# Create a Redis connection
redis_connection = redis.StrictRedis(host=redis_host, port=redis_port, db=redis_db)

# Callback function when a message is received
def on_message(client, userdata, message):
    print(f"Received message on topic '{message.topic}': {message.payload.decode()}")

    # Store the message in Redis list
    redis_connection.lpush(message.topic, message.payload.decode())

    # Keep only the latest 10 messages in the list
    redis_connection.ltrim(message.topic, 0, 9)

    # Publish the message to the topic for other subscribers
    client.publish(message.topic, message.payload)

# Create a MQTT client instance
client = mqtt.Client()

# Set the message received callback
client.on_message = on_message

# Connect to the MQTT broker
client.connect(broker_address, broker_port)

# Subscribe to the list of topics
topics_to_subscribe = ["sensors/temperature", "sensors/humidity"]
for topic in topics_to_subscribe:
    client.subscribe(topic)

# Start the MQTT loop to handle incoming messages
client.loop_forever()

# Keep the script running
try:
    while True:
        pass
except KeyboardInterrupt:
    # Disconnect from the MQTT broker on Ctrl+C
    client.disconnect()
