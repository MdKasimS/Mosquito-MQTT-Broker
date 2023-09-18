from fastapi import FastAPI
import config

# Global Data:- Start
CONFIG = config.CONFIG
mongo = config.CLIENT

db = mongo[CONFIG["database_name"]]
sensor_data = db[CONFIG["collection_list"][2]]

# Global Data:- End


app = FastAPI()
sensor_id = 11

@app.get("/")
def read_root():
    return {"Exalens": "IoT Network Management Tool!"}

@app.get("/sensor-data/{sensor_id}")
async def get_sensor_data(sensor_id: int):
    try:
        # Retrieve sensor data from MongoDB based on sensor_id
        cursor = sensor_data.find({"sensor_id": sensor_id})
        sensorData = []
        for i in cursor:
            i.pop("_id")
            sensorData.append(i)

        if not sensorData:
            return {"message": "No sensor data found for sensor_id {}".format(sensor_id)}

        return {"sensor_data": sensorData}
    
    except Exception as e:
        print("Error in get_sensor_data()...", e)
