import json

def loadSettings(filePath):
    with open(filePath) as file:
        return json.load(file)
    
#Constants
FILEPATH = "./settings.json"



configuration = loadSettings(FILEPATH)






# Tests 
print("Test : ",configuration)