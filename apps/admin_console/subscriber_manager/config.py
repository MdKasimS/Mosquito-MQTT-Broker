import json
import sys
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def loadSettings(filePath):
    with open(filePath) as file:
        return json.load(file)


# Constants
FILEPATH = "./configuration.json"
CONFIG = loadSettings(FILEPATH)
# CLIENT = MongoClient(CONFIG["database_address"])


def connectDatabase():
    
    # Attempt to connect to the MongoDB cluster
    client = MongoClient(CONFIG["database_address"])
    try:
        # Check if the connection was successful
        if client.server_info():
            input("Connected to MongoDB cluster successfully. Press Enter to continue...")
            return client
    except ServerSelectionTimeoutError as e:
        # Handle the ServerSelectionTimeoutError
        # print(f"Error: {e}")
        print("Failed to connect to MongoDB cluster.\nError: [ServerSelectionTimedOut]")
        sys.exit(0)
    except Exception as e:
        # Handle other exceptions that may occur during the    connection  attempt
        print(f"Error: {e}")

