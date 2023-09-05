import threading
import time

# Event to control thread switching
switch_event = threading.Event()

controlNum = None
# Function for Thread 1


def thread_1_function():
    try:
        while True:
            # print("Thread 1 is running")
            time.sleep(1)
            switch_event.wait()  # Wait until signaled to switch
            switch_event.clear()  # Clear the event to allow    Thread 2 to run
    except KeyboardInterrupt:
        # Optionally, you can stop the threads gracefully if needed
        print("Thread1 stopped")
        input("I am waiting")
        thread_1.join()

# Function for Thread 2


def thread_2_function():
    try:
        while True:
            # print("Thread 2 is running")
            time.sleep(1)
            switch_event.set()  # Signal Thread 1 to switch
            switch_event.wait()  # Wait until signaled to switch
            switch_event.clear()  # Clear the event to allow    Thread 1 to run
    except KeyboardInterrupt:
        # Optionally, you can stop the threads gracefully if needed
        print("Thread2 stopped")
        input("I am waiting")
        thread_2.join()


# Create and start Thread 1
thread_1 = threading.Thread(target=thread_1_function)
thread_1.start()

# Create and start Thread 2
thread_2 = threading.Thread(target=thread_2_function)
thread_2.start()

# Main thread
try:
    while True:
        # Perform main thread tasks
        time.sleep(2)
        print("Main thread is running")

except KeyboardInterrupt:
    # Optionally, you can stop the threads gracefully if needed
    print("Main thread stopped")
    # global controlNum
    input("I am waiting")
    thread_1.join()
    thread_2.join()
