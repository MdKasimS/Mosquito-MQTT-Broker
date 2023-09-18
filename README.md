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
  - pip install paho-mqtt
  - pip install pymongo
  - pip install redis
  - pip install fastapi uvicorn

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

Author:-
- Mahamadkasim Sache
- https://github.com/MdKasimS
- https://www.linkedin.com/in/mahamadkasim-sache

![Screenshot (283)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/f90cf6e2-ace3-49db-a5ea-0d345786496a)
![Screenshot (288)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/29694303-5c25-496a-82ca-13d373890e6f)
![Screenshot (287)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/9b159f9d-7c87-4379-be50-980b0b4ed37b)
![Screenshot (286)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/3ed99f18-8106-481f-a426-5992e8f033f3)
![Screenshot (285)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/ef964a79-1116-4db2-b653-294bedaac190)
![Screenshot (284)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/994c09f0-fad0-4722-9052-1cc66c167319)

![Screenshot (289)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/14e5eb8c-8e37-42e2-811f-aa17d87dc4e1)
![Screenshot (291)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/fbacf49e-8e54-43ad-b904-d8f1859b5b92)
![Screenshot (290)](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/59de4ec1-92e6-4b4f-9c87-04110874ea65)
