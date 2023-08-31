import threading
import broker
from config import configuration as config



if __name__ == "__main__":
    print(config)

    pid = broker.initBroker(config["start"])

    print(pid)

    broker_pid = broker.get_pid_by_name(config["process_name"])

    print(broker_pid)
    input(f"Check {broker_pid} in task manager for mosquitto")

    input("Should I kill?")
    if broker_pid is not None:
        broker.closeBroker(broker_pid)
    else:
        print(f'Process {config["process_name"]} not found.')
