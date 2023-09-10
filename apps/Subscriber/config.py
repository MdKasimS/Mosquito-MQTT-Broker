import json
import sys
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
            print("Connected to MongoDB cluster successfully. Press Enter to continue...")
            return client
    except ServerSelectionTimeoutError as e:
        # Handle the ServerSelectionTimeoutError
        print("Failed to connect to MongoDB cluster.\nError: [ServerSelectionTimedOut]")
        sys.exit(0)
    except Exception as e:
        # Handle other exceptions that may occur during the    connection  attempt
        print(f"Error: {e}")

# Constants
FILEPATH_SET = "./../../settings.json"
FILEPATH_CON = "./configurations.json"
CONFIG = loadSettings(FILEPATH_SET)
CLIENT = connectDatabase()


