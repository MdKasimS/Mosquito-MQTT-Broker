import json
import sys
import time
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


def loadSettings(filePath):
    with open(filePath) as file:
        return json.load(file)


def connectDatabase():
    
    # Attempt to connect to the MongoDB cluster
    client = MongoClient(CONFIG["database_address"])
    try:
        # Check if the connection was successful
        if client.server_info():
            input("Connected to MongoDB cluster successfully. Press Enter to continue...")
            CONFIG["db_connection"] = "Connected"
            return client
    except ServerSelectionTimeoutError as e:
        # Handle the ServerSelectionTimeoutError
        input("Failed to connect to MongoDB cluster.\nError: [ServerSelectionTimedOut\n\nPress Enter To Continue...")
        sys.exit(0)
    except Exception as e:
        # Handle other exceptions that may occur during the    connection  attempt
        print(f"Error: {e}")





# Constants
CONFIG_FILEPATH = "./configuration.json"
SETTING_FILEPATH = "../../settings.json"
CONFIG = loadSettings(CONFIG_FILEPATH)
SETTING = loadSettings(SETTING_FILEPATH)
CLIENT = connectDatabase()




# Tests
# print("Test : ", configuration)
