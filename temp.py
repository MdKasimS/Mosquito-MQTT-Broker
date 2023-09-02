import threading
import random
import time

# Function to simulate a sensor and write data to a text file
def simulate_sensor(sensor_id):
    while True:
        # Simulate sensor data
        sensor_data = random.randint(0, 100)
        
        # Generate a unique filename for each sensor
        filename = f"sensor_{sensor_id}.txt"
        
        # Write data to the text file
        with open(filename, "a") as file:
            file.write(f"Sensor-{sensor_id} Data: {sensor_data}\n")
        
        # Sleep for a while before the next reading
        time.sleep(1)

# Create and start multiple threads for simulating sensors
num_sensors = 3
sensor_threads = []

for i in range(num_sensors):
    thread = threading.Thread(target=simulate_sensor, args=(i,))
    sensor_threads.append(thread)
    thread.start()

# Wait for all sensor threads to complete (this will never be reached)
for thread in sensor_threads:
    thread.join()

