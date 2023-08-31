def send(msg, sub):
    # httpResponse code
    pass

def listen(portNumber):
    # httpRequest code
    # return msg
    pass

def pop(topic):
    pass

# This is a data structure which will act as Queue for messages
topicsAndMessages = {
    {
        "topic1": ['msg1', 'msg1', 'msg1', 'msg1', 'msg1']
    },
    {
        "topic2": []
    }
}

publishers = [      # A data structure which store publishers names
    {
    "publisher1": ["topic1"],
    "publisher2":["topic2"]
    }
]

subscribers = [     # A data structure which store subscribers names
    {
    "subscriber1": ["topic1", "topic2"],
    "subscriber2":["topic1"]
    }
]

msgPack = {
    "topic": "topic1",
    "message": "15.30"
}

print(msgPack["topic"])

# while 1:    # Event loop which processes asychronously

    # msgPack = listen(1800)    
print(topicsAndMessages["topic1"]) #.append(msgPack["message"])