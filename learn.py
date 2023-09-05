import os
import random
import sys
import threading
from time import sleep
import time


# Thread creation and IDs


def threadBasic():
    def task():
        print("I am Thread")

    thread = threading.Thread(target=task)
    thread1 = threading.Thread(target=task)
    thread.start()
    thread1.start()
    print(thread, "=", thread.ident, end="")
    sleep(5)
    print(thread1, "-", thread1.ident, end="")
    thread.join()
    thread1.join()

# Multiple thread on same resource with lock


def incrementCheck():

    # Shared resource
    shared_counter = 0

    # Lock for synchronization
    lock = threading.Lock()

    # Function to increment the shared counter

    def increment_counter():
        global shared_counter
        for _ in range(100000):
            with lock:
                shared_counter += 1

    # Create multiple threads
    threads = []

    for _ in range(4):
        thread = threading.Thread(target=increment_counter)
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    print(f"Shared counter value: {shared_counter}")

    print(lock)

# Thread IDs. not sure of are they exactly same to os PIDs


def threadIdents():

    def print_thread_id():
        thread_id = threading.get_ident()
        print(f"Thread ID: {thread_id}")

    # Create and start two threads
    thread1 = threading.Thread(target=print_thread_id)
    thread2 = threading.Thread(target=print_thread_id)

    thread1.start()
    thread2.start()

    # Wait for both threads to complete
    thread1.join()
    thread2.join()


def threadPIDs():

    def runProgram(program_name):
        os.system(program_name)

    thread = threading.Thread(target=runProgram, args=["mosquitto"])
    thread1 = threading.Thread(target=runProgram, args=["notepad"])

    thread.start()
    thread1.start()

    print(f"{thread}  =>Thread id : ", thread.ident)
    print(f"{thread1} =>Thread id : ", thread1.ident)
    # Wait for both threads to complete
    thread.join()
    thread1.join()

    print(f"{thread}  =>Thread id : ", thread.ident)
    print(f"{thread1} =>Thread id : ", thread1.ident)


def codeAfterThread():
    close = 0

    def simulate_sensor(sensor_id):
        # input(close)

        while True:
            if close != 5:
                # Simulate sensor data
                sensor_data = 35 + random.randint(0, 100)/100 % 30

                # Generate a unique filename for    each sensor
                filename = f"sensor_{sensor_id}.txt"

                # Write data to the text file
                with open(filename, "a") as file:
                    file.write(f"Sensor-{sensor_id} Data:{sensor_data}\n")

                    # Sleep for a while before the  next     reading
                    time.sleep(1)
            else:
                break
        print(f"Exiting thread {sensor_id}")

    num_sensors = 3
    sensor_threads = []

    for i in range(num_sensors):
        print(f"{i} thread started...")
        thread = threading.Thread(target=simulate_sensor,   args=(i,))
        sensor_threads.append(thread)
        thread.start()

    # Wait for all sensor threads to complete (this will never be reached)
    # for thread in sensor_threads:
    #     thread.join()

    input()
    os.system("cls")

    choice = 0
    close += 1

    while choice != 5:
        print("1. Kasim \n2. Sache \n3.Alhamdulillah")
        choice = int(input("Enter Your Choice : "))
        if choice == 5:
            close = choice
        os.system("cls")

    print("Closing program...")
    sys.exit(0)


# Function for the thread
def threadControl():
    def my_thread_function():
        while True:
            print("Thread is running")
            time.sleep(1)

    # Create and start the thread
    my_thread = threading.Thread(target=my_thread_function)
    my_thread.start()

    # Main program loop
    while True:
        # Check the thread's status
        if not my_thread.is_alive():
            break  # Exit the loop if the thread has finished
        else:
            print("Main program continues...")
            time.sleep(2)  # Sleep or do other work as needed

    print("Main program exits")


# threadBasic()
# threadIdents()
# threadPIDs()
# threadControl()
codeAfterThread()
