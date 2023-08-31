QTT_ERR_AGAIN = -1
MQTT_ERR_SUCCESS = 0
MQTT_ERR_NOMEM = 1
MQTT_ERR_PROTOCOL = 2
MQTT_ERR_INVAL = 3
MQTT_ERR_NO_CONN = 4
MQTT_ERR_CONN_REFUSED = 5
MQTT_ERR_NOT_FOUND = 6
MQTT_ERR_CONN_LOST = 7
MQTT_ERR_TLS = 8
MQTT_ERR_PAYLOAD_SIZE = 9
MQTT_ERR_NOT_SUPPORTED = 10
MQTT_ERR_AUTH = 11
MQTT_ERR_ACL_DENIED = 12
MQTT_ERR_UNKNOWN = 13
MQTT_ERR_ERRNO = 14
MQTT_ERR_QUEUE_SIZE = 15
MQTT_ERR_KEEPALIVE = 16


CONNACK_ACCEPTED = 0
CONNACK_REFUSED_PROTOCOL_VERSION = 1
CONNACK_REFUSED_IDENTIFIER_REJECTED = 2
CONNACK_REFUSED_SERVER_UNAVAILABLE = 3
CONNACK_REFUSED_BAD_USERNAME_PASSWORD = 4
CONNACK_REFUSED_NOT_AUTHORIZED = 5

def error_string(mqtt_errno):
    """ the error string associated with an mqtt error number."""
    
    error_messages ={    
        MQTT_ERR_SUCCESS: "No error.",
        MQTT_ERR_NOMEM: "Out of memory.",
        MQTT_ERR_PROTOCOL: "A network protocol error occurred when communicating with the broker.",
        MQTT_ERR_INVAL: "Invalid function arguments provided.",
        MQTT_ERR_NO_CONN: "The client is not currently connected.",
        MQTT_ERR_CONN_REFUSED: "The connection was refused.",
        MQTT_ERR_NOT_FOUND: "Message not found (internal error).",
        MQTT_ERR_CONN_LOST: "The connection was lost.",
        MQTT_ERR_TLS:"A TLS error occurred.",
        MQTT_ERR_PAYLOAD_SIZE: "Payload too large.",
        MQTT_ERR_NOT_SUPPORTED: "This feature is not supported.",
        MQTT_ERR_AUTH: "Authorisation failed.",
        MQTT_ERR_ACL_DENIED: "Access denied by ACL.",
        MQTT_ERR_UNKNOWN: "Unknown error.",
        MQTT_ERR_ERRNO: "Error defined by errno.",
        MQTT_ERR_QUEUE_SIZE: "Message queue full.",
        MQTT_ERR_KEEPALIVE: "Client or broker did not communicate in the keepalive interval."
    }
    
    if mqtt_errno in error_messages.keys():
        return error_messages[mqtt_errno]
    else:
        return "Unknown error."

def connack_string(connack_code):
    """Return the string associated with a CONNACK result."""
    connack_messages = {
    CONNACK_ACCEPTED: "Connection Accepted.",
    CONNACK_REFUSED_PROTOCOL_VERSION:  "Connection Refused: unacceptable protocol version.",
    CONNACK_REFUSED_IDENTIFIER_REJECTED:  "Connection Refused: identifier rejected.",
    CONNACK_REFUSED_SERVER_UNAVAILABLE:  "Connection Refused: broker unavailable.",
    CONNACK_REFUSED_BAD_USERNAME_PASSWORD:  "Connection Refused: bad user name or password.",
    CONNACK_REFUSED_NOT_AUTHORIZED:  "Connection Refused: not authorised."
    }
    
    if connack_code in connack_messages.keys():
        return connack_messages[connack_code]
    else:
        return "Connection Refused: unknown reason."


#test code
# for i in range(1,20):
#     print(error_string(i))

# for i in range(1,20):
#     print(connack_string(i))