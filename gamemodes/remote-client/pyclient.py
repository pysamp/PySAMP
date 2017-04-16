""" Implements client for pysamp-remote-server
{type:'callback', data:''} """
import websocket
import json
import thread
import time

CALLBACKS = {}

def __on_message(ws, message):
    action = json.loads(message)
    print message

def __on_error(ws, error):
    print error

def __on_close(ws):
    print "### closed ###"

def __on_open(ws):
    None

def add_callback(callback, closure):
    if not CALLBACKS.has_key(callback):
        CALLBACKS[callback] = []
    CALLBACKS[callback].append(closure)

def connect(ip_adress, port):
    """ establishes websocket connection """
    if __name__ == "__main__":
        websocket.enableTrace(True)
        connection = websocket.WebSocketApp("ws://"+ip_adress+":"+port+"/",
                                            on_message=__on_message,
                                            on_error=__on_error,
                                            on_close=__on_close)
        connection.on_open = __on_open
        connection.run_forever()

