# Mosquito-MQTT-IoT-Application

This is a IoT netwok management tool which uses Mosquitto Server as MQTT broker for publishing and subscribing for messages.
In this sensors as MQTT clients are acting as publishers publishing sensor value in {"sensor_id": <unique_id>, "value" : <sensor_reading>, "timestamp": <IO8601_Formatted_Timestamp> } format.

It contains apps as follows:
  1. Mosquitto broker manager - ./main.py
  2. Mosquitto publisher - apps/admin_console/main.py
  3. Mosquitto subscriber - apps/subscriber/main.py
  4. FastAPI endpoint app - apps/fast_api/main.py
  5. Dashboard app - apps/dashboard/     ----------> [Coming soon]
It also implements Redis Cache to store first 10 messages in queues named as sensors/temperature and sensors/humidity.

Design of this system is stored in Mosquitto-MQTT-IoT-Application.drawio file.
It also have how control is flowing, how messages travel in system.

How to start this application? Instruction -

1. Install MongoDb database locally and keep its settings to default.
2. Download Docker application.
3. Download official redis.redis-stack dockerfile to setup redis cache.
4. Install Python 3.10 from official site
5. Install paackges - pymongo, redis, paho-mqtt and fast-api using command like
  - pip install redis pymongo
  - pip install paho-mqtt
  - pi pinstall fast-api

6. Run startup.py file to setup database collections
7. Adjust indexes for sensor IDs
8. Start mongo db server
9. Start Redis server by running image redis/redis-stack
10. Start MQTT broker using ./main.py file
11. Start admin-console app which is simulated sensors as MQTT publisher client
12. Strat subscriber app by running apps/subscriber/main.py
13. Observe redis data with list named as sensors/humidity and sensors/temeperature.
14. Start FastApi app by running apps/fast_api/main.py


More advanced controlling features coming soon....


