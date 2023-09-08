import random
import time
from bson import ObjectId

from prettytable import PrettyTable

from .utility import clearScreen
from .utility import WelcomeNote
from .utility import Exit
from .config import CONFIG as config, CLIENT as client
from pymongo import DESCENDING
from pymongo.errors import BulkWriteError

from database import crud
from database import data


db = client[config["database_name"]]
collection = db["sensors"]


def getMenuList():
    return ["Add Sensor", "View Sensor", "Update Sensor", "Delete Sensor", "Restart Sensor", "Turnoff Sensor", "Exit"]

def Switch(choice):
    action = {
        1: AddSensor,    # all sensors
        2: ViewSensor,   # active sensors
        3: UpdateSensor,  # all sensors
        4: DeleteSensor,  # all sensors
        5: RestartSensor,  # all sensors & active sensors
        6: TurnOnSensor,  # all sensors
        7: TurnOffSensor,  # active sensors
        8: Exit
    }
    if choice in action.keys():
        return action[choice]
    else:
        clearScreen()
        input("Enter the valid choice. Press enter to continue")

def AddSensor():
    
    last_record = collection.find_one({}, sort=[('sensor_id',DESCENDING)])
    nextId = last_record["sensor_id"] + 1
    
    choice = 0
    sensor = {
        "sensor_id" : nextId
        }
    
    while choice!= 3:
        WelcomeNote()
        print("1. Add One\n2. Add Multiple\n3. Go Back")
        
        try:
            choice = int(input("Enter your choice:"))
            clearScreen()
            if choice == 3:
                return
        except:
            clearScreen()
            input("Enter the valid choice. Press enter to continue")
            continue

        # For inserting one record
        if choice == 1:
            sensor = acceptSensorData(sensor)
            if sensor is not None:
                collection.insert_one(sensor)
            else:
                clearScreen()
                input("Unexpected Error Occured. Press enter to continue...")
                return
        # For inserting many records
        else:
            flag = True
            records = []
            while flag is True:
                WelcomeNote()
                try:
                    num = input("Enter number of records :")
                    flag = False
                except Exception as e:
                    clearScreen()
                    input("Please Enter Integre Value >0. Press Enter To Continue...")
                    continue
                num = int(num)
                for i in range(num):
                    sensor = acceptSensorData(sensor)
                    if sensor is not None:
                        records.append(sensor)
                    else:
                        input("Unexepected Error Occured...")
                
                if len(records)>0:
                    collection.insert_many(records) #Not Working For BULK Writes 



    clearScreen()
    input("Sensor Has Been Successfully Added!\nPress Enter To Continue")
    # clearScreen()

def ViewSensor():
    clearScreen()
    
    tableColumnHeadings = []    # "_id","sensor_id","type","topic","publisher","subscriber","default","status"

    for i in data.ACTIVE_SENSORS[0].keys():
        tableColumnHeadings.append(i)    

    # tableColumnHeadings.append("Sr_No")
    table = PrettyTable(tableColumnHeadings)

    # for row in data.ACTIVE_SENSORS:
    #     table.add_row([row["_id"],row["sensor_id"],row["type"],row["topic"],row["publisher"], row["subscriber"], row["default"], row["status"]])

    for row in data.ACTIVE_SENSORS:
        table.add_row([
            row[tableColumnHeadings[0]],
            row[tableColumnHeadings[1]],
            row[tableColumnHeadings[2]],
            row[tableColumnHeadings[3]],
            row[tableColumnHeadings[4]],
            row[tableColumnHeadings[5]],
            row[tableColumnHeadings[6]],
            row[tableColumnHeadings[7]]])
    
    for i in tableColumnHeadings:
        table.align[i] = "c"

    table.align["topic"] = "l"
    print(table)

    input("\nPress Enter To Continue...")

def UpdateSensor():
    pass

def RestartSensor():
    pass

def DeleteSensor():
    pass

def TurnOnSensor():
    pass

def TurnOffSensor():
    pass

def getSensors():
    return data.ACTIVE_SENSORS

def acceptSensorData(sensor):
    type = ["Default", "Runtime"]
    channels = ["test/", "prod/"]

    try:  
        # Get Sensor Type
        print("Choose Type:\n1. Default\n2. Runtime\n")
        value = input("Enter Your Choice : ")
        
        if value in [1,2]:
            sensor["type"] = type[value]
        else:
            sensor["type"] = "default"


        # Get Sensor topic
        print("\nChoose Publish At :\n1. test\n2. prod")
        channel = input("Enter your choice : ")
        value = input("Enter your topic name : ")

        if channel == "2":
            sensor["topic"] = channels[1] + value
        else:
            sensor["topic"] = "test/" + value

        sensor["publisher"] = True
        sensor["subscriber"] = False

        # Get default sensor value
        value = float(input("Enter default sensor value : "))
        sensor["default"] = value
        
        # Set sensor
        sensor["status"] = True
            
        return sensor

    except Exception as e:
        clearScreen()
        key = 0
        value = 0
        input(f"Sensors can't be of same details -> {key}:{value}\nPress enter tocontinue...")
        return None
    
def Menu():
    clearScreen()
    choice = ""
    # Database()
    
    if client.server_info():
        while choice != len(getMenuList()):
            WelcomeNote()

            for counter, option in enumerate(getMenuList()):
                print(f"{counter+1}.{option}")

            try:
                choice = int(input("Enter your choice:"))
            except:
                clearScreen()
                input("Enter the valid choice. Press enter  to  continue")
                continue

            execute = Switch(choice)

            if execute is not None:
                execute()

    else:
        clearScreen()
        input("Server Disconnected. Please Press Enter To Continue..")
        return
