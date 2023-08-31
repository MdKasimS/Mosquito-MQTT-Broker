import os

command = ""

while 1:
    command = input("Enter your message : ")
    if command == "exit":
        print('Terminating session....')
        break

    message = 'mosquitto_pub -h localhost -t test/topic -m '
    comand = message + '"' + command +'"'
    os.system(comand)
