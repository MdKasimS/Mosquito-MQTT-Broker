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


data2 = [
{'sensor_id': 21, 'value': 87.83, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 38, 373635)},
{'sensor_id': 15, 'value': 34.9, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 38, 658652)},{'sensor_id': 17, 'value': 69.71, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 39, 557603)},
{'sensor_id': 11, 'value': 41.19, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 40, 566888)},
{'sensor_id': 19, 'value': 41.65, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 40, 566888)},
{'sensor_id': 12, 'value': 15.75, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 41, 577121)},
{'sensor_id': 17, 'value': 69.53, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 41, 578097)},
{'sensor_id': 16, 'value': 67.17, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 42, 589222)},
{'sensor_id': 19, 'value': 41.4, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 42, 589222)},{'sensor_id': 12, 'value': 15.53, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 43, 599929)},
{'sensor_id': 18, 'value': 31.27, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 44, 607803)},
{'sensor_id': 14, 'value': 36.77, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 44, 719209)},
{'sensor_id': 20, 'value': 46.23, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 45, 619749)},
{'sensor_id': 13, 'value': 25.88, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 46, 451598)},
{'sensor_id': 19, 'value': 41.3, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 46, 637261)},{'sensor_id': 11, 'value': 40.82, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 47, 647565)},
{'sensor_id': 17, 'value': 69.63, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 47, 646599)},
{'sensor_id': 11, 'value': 41.1, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 48, 653967)},{'sensor_id': 20, 'value': 46.49, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 48, 654835)},
{'sensor_id': 12, 'value': 15.79, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 49, 665569)},
{'sensor_id': 18, 'value': 31.24, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 50, 675273)},
{'sensor_id': 14, 'value': 36.8, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 50, 769514)},{'sensor_id': 17, 'value': 69.48, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 51, 684260)},
{'sensor_id': 14, 'value': 36.83, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 51, 778557)},
{'sensor_id': 20, 'value': 46.28, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 52, 697434)},
{'sensor_id': 12, 'value': 15.56, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 53, 707172)},
{'sensor_id': 18, 'value': 31.58, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 53, 707172)},
{'sensor_id': 12, 'value': 15.85, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 54, 720672)},
{'sensor_id': 18, 'value': 31.24, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 55, 727714)},
{'sensor_id': 16, 'value': 67.16, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 55, 728583)},
{'sensor_id': 19, 'value': 41.54, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 56, 744552)},
{'sensor_id': 14, 'value': 36.96, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 56, 838439)},
{'sensor_id': 20, 'value': 46.43, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 57, 754346)},
{'sensor_id': 12, 'value': 15.76, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 57, 756075)},
{'sensor_id': 20, 'value': 46.54, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 58, 760983)},
{'sensor_id': 16, 'value': 67.24, 'timestamp': datetime.datetime(2023, 9, 18, 8, 3, 59, 770295)},
{'sensor_id': 22, 'value': 51.42, 'timestamp': datetime.datetime(2023, 9, 18, 8, 4, 0, 572234)},{'sensor_id': 11, 'value': 41.08, 'timestamp': datetime.datetime(2023, 9, 18, 8, 4, 0, 775555)},{'sensor_id': 21, 'value': 87.82, 'timestamp': datetime.datetime(2023, 9, 18, 8, 4, 1, 579884)},{'sensor_id': 11, 'value': 41.18, 'timestamp': datetime.datetime(2023, 9, 18, 8, 4, 1, 785775)},{'sensor_id': 22, 'value': 51.43, 'timestamp': datetime.datetime(2023, 9, 18, 8, 4, 2, 588422)}
] 

for i in data2:
    print(i['sensor_id'], i['value'], i['timestamp'])

    document = {
        "timestamp": i['timestamp'],#{"$date":bson_utc_datetime},
        "sensor_id": i['sensor_id'],
        "value": i['value']
    }
    print(document)
    sensor_data.insert_one(document)
