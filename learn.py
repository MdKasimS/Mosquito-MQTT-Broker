import threading


def task():
    print("I am Thread")


# thread = threading.Thread(target=task)
# thread1 = threading.Thread(target=task)
# print(thread)
# print(thread1)


# print(thread.native_id)


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
