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


Design Overview :
1. 'admin-console' app is publisher and manager app. Its a menu driven console application.
2. 'subscriber' app is a subscriber app which subscribe to MQTT publisher channels and receive messages from broker.
3. Sensors are simulated using threads in apps/admin-console. I have created threads which are centrally being controlled using variable named THREADCONTROL in whole solution.
4. Sensors publish data on respective channel and store its log in 'sensor_{id}.txt' files. Sensors are MQTT Publisher clients
5. Published messages by sensor threads are received by subscriber app which stores them in queues named sensors/temeparture and sensors/humidty. Both these queues are of size 10.
6. Subscriber app after storing messags in redis cache, publishes to redis channels one by one by popping out messages.
7. In admin-console app, redis subscriber subscribes to redic channels and receives messages which are later stored in MongoDB database.
8. FastAPI end point fetches data from MongoDB for given sensor id.

Challenges:
1. Understaing Mosquitto and MQTT
2. Installing redis specially on Windos using Docker
3. Creating complex mechanism to handle exceptions and thread execution code.
4. Handling asynchrous calls.
5. Debugging thread codes and reading sensor logs

Here is system architecture:-
![image](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/83fce8e9-dbcc-41bf-8a9e-a83f4db1689a)

Here is stages of development:-
![image](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/e19e9025-58a4-4f56-86c9-4a943fb4c827)

Here is block diagram:-
![image](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/c1a72dd7-f5a2-4d93-aa46-ca42d5c0746c)

Here is functional block diagram:-
![image](https://github.com/MdKasimS/Mosquito-MQTT-IoT-Application/assets/45384577/a2e61aec-af88-4947-98b8-c20878f4581b)

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
