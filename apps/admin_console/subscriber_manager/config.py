import json
from pymongo import MongoClient


def loadSettings(filePath):
    with open(filePath) as file:
        return json.load(file)


# Constants
FILEPATH = "./configuration.json"
CONFIG = loadSettings(FILEPATH)
CLIENT = MongoClient(CONFIG["database_address"])


# Tests
# print("Test : ", configuration)
