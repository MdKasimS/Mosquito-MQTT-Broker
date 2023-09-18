from pymongo import MongoClient
from bson import ObjectId
import datetime

client = MongoClient("mongodb://127.0.0.1:27017/")
db = client["iot_data"]
sensor_data = db["sensor_data"]

data = [
    {'sensor_id': 11, 'value': 41.19, 'timestamp': '2023-09-18T00:16:05.516163'},
    {'sensor_id': 11, 'value': 41.01, 'timestamp': '2023-09-18T00:16:06.530151'},
    {'sensor_id': 11, 'value': 41.15, 'timestamp': '2023-09-18T00:16:07.545220'},
    {'sensor_id': 11, 'value': 40.95, 'timestamp': '2023-09-18T00:16:08.552679'},
    {'sensor_id': 11, 'value': 41.08, 'timestamp': '2023-09-18T00:16:09.562287'},
    {'sensor_id': 11, 'value': 40.96, 'timestamp': '2023-09-18T00:16:10.572862'},
    {'sensor_id': 11, 'value': 41.05, 'timestamp': '2023-09-18T00:16:11.590960'},
    {'sensor_id': 11, 'value': 41.0, 'timestamp': '2023-09-18T00:16:12.597419'},
    {'sensor_id': 14, 'value': 36.99, 'timestamp': '2023-09-18T09:11:51.630444'},
    {'sensor_id': 14, 'value': 36.93, 'timestamp': '2023-09-18T09:16:53.209437'},
    {'sensor_id': 14, 'value': 36.51, 'timestamp': '2023-09-18T09:16:54.227240'},
    {'sensor_id': 14, 'value': 36.52, 'timestamp': '2023-09-18T09:16:55.238603'},
    {'sensor_id': 14, 'value': 36.99, 'timestamp': '2023-09-18T09:16:57.301859'},
    {'sensor_id': 14, 'value': 36.82, 'timestamp': '2023-09-18T09:16:58.327610'},
    {'sensor_id': 14, 'value': 36.83, 'timestamp': '2023-09-18T09:16:59.358550'},
    {'sensor_id': 14, 'value': 36.57, 'timestamp': '2023-09-18T09:17:00.370425'},
    {'sensor_id': 14, 'value': 36.77, 'timestamp': '2023-09-18T09:17:01.484095'},
    {'sensor_id': 21, 'value': 87.86, 'timestamp': '2023-09-18T00:16:12.565417'},
    {'sensor_id': 21, 'value': 87.93, 'timestamp': '2023-09-18T00:16:13.579820'},
    {'sensor_id': 21, 'value': 87.74, 'timestamp': '2023-09-18T00:16:14.588991'},
    {'sensor_id': 21, 'value': 87.76, 'timestamp': '2023-09-18T00:16:15.599905'},
    {'sensor_id': 21, 'value': 88.07, 'timestamp': '2023-09-18T00:16:16.608855'},
    {'sensor_id': 21, 'value': 87.77, 'timestamp': '2023-09-18T00:16:17.620983'},
    {'sensor_id': 21, 'value': 87.95, 'timestamp': '2023-09-18T00:16:18.630655'},
    {'sensor_id': 21, 'value': 88.05, 'timestamp': '2023-09-18T00:16:19.637667'},
    {'sensor_id': 22, 'value': 51.47, 'timestamp': '2023-09-18T09:16:58.324610'},
    {'sensor_id': 22, 'value': 51.43, 'timestamp': '2023-09-18T09:16:59.351552'},
    {'sensor_id': 22, 'value': 51.63, 'timestamp': '2023-09-18T09:17:00.368400'},
    {'sensor_id': 22, 'value': 51.87, 'timestamp': '2023-09-18T09:17:01.484095'},
    {'sensor_id': 22, 'value': 51.87, 'timestamp': '2023-09-18T09:17:02.495812'},
    {'sensor_id': 22, 'value': 51.61, 'timestamp': '2023-09-18T09:17:03.508158'},
    {'sensor_id': 13, 'value': 25.81, 'timestamp': '2023-09-18T00:16:06.530151'},
    {'sensor_id': 13, 'value': 25.82, 'timestamp': '2023-09-18T00:16:07.545220'},
    {'sensor_id': 13, 'value': 25.76, 'timestamp': '2023-09-18T00:16:08.551678'},
    {'sensor_id': 13, 'value': 25.86, 'timestamp': '2023-09-18T00:16:09.561288'},
    {'sensor_id': 13, 'value': 25.93, 'timestamp': '2023-09-18T00:16:10.571849'},
    {'sensor_id': 13, 'value': 25.98, 'timestamp': '2023-09-18T00:16:11.589959'},
    {'sensor_id': 13, 'value': 25.77, 'timestamp': '2023-09-18T00:16:12.596418'},
]

for i in data:
    print(i['sensor_id'], i['value'], i['timestamp'])
    stamp = datetime.datetime.fromisoformat(i['timestamp'])
    print(type(stamp))
    bson_utc_datetime = ObjectId.from_datetime(stamp)
    print(type(bson_utc_datetime))

    document = {
        "timestamp": datetime.datetime.utcnow(),#{"$date":bson_utc_datetime},
        "sensor_id": i['sensor_id'],
        "value": i['value']
    }
    print(document)
    sensor_data.insert_one(document)
