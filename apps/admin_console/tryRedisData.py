import redis

from config import CONFIG as config, CLIENT as client

def redis_cache():
    redis_host = config["redis_address"]
    redis_port = config["redis_port"]
    redis_db = config["redis_db"][0]

    print(f"Redis details are : {redis_host}, {redis_port} {redis_db}")



# Global data : Start

redis_host = config["redis_address"]
redis_port = config["redis_port"]
redis_db = config["redis_db"][0]

# Connect to the Redis server
redis_connection = redis.StrictRedis(host= redis_host, port= redis_port, db = redis_db)

# Global data : End




def main():

    # Select the desired database (db=0)
    global redis_connection
    # redis_connection.select(redis_db)

    all_keys = redis_connection.keys('*')

    # Print the list of keys
    for key in all_keys:
        print(key.decode())

    redis_cache()
    
    # Get all keys in the selected database
    keys_in_db_0 = redis_connection.keys('*')  # You can use a pattern like '*' to match all keys

    # Print the list of keys
    for key in keys_in_db_0:
        print(key.decode())  # Decode bytes to strings


    # Define the key(s) you want to continuously monitor
    key_to_monitor = "your_key_name"


    # for i in sensor_data.keys():
        #     # Retrieve a value by key
        #     value = redis_connection.get(i)
        #     print(value.decode())  # Decode bytes to a string

    pass
    

# while True:
#     # Get the value associated with the key
#     value = redis_connection.get(key_to_monitor)

#     if value is not None:
#         print(f"Value for key '{key_to_monitor}': {value.decode()}")

#     # Optional: Add a sleep to control the polling frequency
#     time.sleep(1)  # Sleep for 1 second (adjust as needed)

if __name__ == "__main__":
    main()