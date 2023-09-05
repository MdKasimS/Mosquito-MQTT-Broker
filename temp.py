import threading
import random
import time
import queue

# Function to simulate a sensor and generate data


def simulate_sensor(sensor_id, output_queue):
    while True:
        sensor_data = random.randint(0, 100)
        output_queue.put((sensor_id, sensor_data))
        time.sleep(1)

# Function to display the output of a selected sensor


def display_sensor_output(selected_sensor, output_queue):
    while True:
        sensor_id, sensor_data = output_queue.get()
        if sensor_id == selected_sensor:
            print(f"Sensor-{sensor_id} Data: {sensor_data}")
        output_queue.task_done()


# Create a shared output queue
output_queue = queue.Queue()

# Create and start sensor threads
num_sensors = 5
sensor_threads = []

for i in range(num_sensors):
    thread = threading.Thread(target=simulate_sensor, args=(i, output_queue))
    sensor_threads.append(thread)
    thread.start()

selected_sensor = None
while selected_sensor != 8:
    # Create a display thread (for displaying the selected sensor's output)
    selected_sensor = int(input("Enter Sensor Id <5:"))
    # selected_sensor = 0  # Change this to the desired sensor ID
    display_thread = threading.Thread(
        target=display_sensor_output, args=(selected_sensor, output_queue))
    display_thread.start()

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        continue

# Main thread continues running
# while True:
#     try:
#         time.sleep(1)
#     except KeyboardInterrupt:
#         break

# Stop all threads
for thread in sensor_threads:
    thread.join()

output_queue.join()  # Wait for the output queue to be empty
display_thread.join()
