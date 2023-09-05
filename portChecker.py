import socket

hostname = 'localhost'  # Change to the hostname or IP address you want to check
port = 27017  # Change to the port you want to check

try:
    socket.create_connection((hostname, port))
    print(f"Port {port} is open")
except ConnectionRefusedError:
    print(f"Port {port} is closed")
except Exception as e:
    print(f"An error occurred: {e}")
