import broker
from config import configuration as config
    

print(config)

broker.initBroker(config["broker"])


