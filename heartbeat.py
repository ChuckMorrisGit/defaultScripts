#!/usr/bin/env python3

# afutros720_runlevel

import paho.mqtt.client as mqtt
import os
from enum import Enum
import sys

VERSION = "1.0.01"

hostname = os.uname()[1]

mqtt_host="192.168.2.70"

topic_status = "devices/" + hostname + "/status"
topic_runlevel = "devices/" + hostname + "/runlevel"
topic_version = "devices/" + hostname + "/version"
runLevel = ""


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    RUNNING = "running"
    STOPPED = "stopped"
    REBOOTING = "rebooting"
    SHUTTING_DOWN = "shutting down"
    UPDATING = "updating"


def setRunLevel(runlevel):
    global runLevel
    
    runLevel = runlevel
    client.publish(topic_runlevel, runLevel, retain=True)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("devices/" + hostname + "/cmd")
    client.publish(topic_status, Status.ONLINE.value, retain=True)
    client.publish(topic_version, VERSION, retain=True)
    setRunLevel(Status.RUNNING.value)


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode('ascii'))
    
    if payload == "reboot":
        print("Rebooting")
        client.publish(topic_status, Status.REBOOTING.value, retain=True)
        setRunLevel(Status.REBOOTING.value)
        os.system("./reboot.sh &")
        
    if payload == "shutdown":    
        print("Shutting down")
        client.publish(topic_status, Status.SHUTTING_DOWN.value, retain=True)
        setRunLevel(Status.SHUTTING_DOWN.value)
        os.system("./shutdown.sh &")
    
    if payload == "update":
        print("Update request")
        client.publish(topic_status, Status.UPDATING.value, retain=True)
        setRunLevel(Status.UPDATING.value)
        os.system("./upgrade.sh &")

    if payload == "status":
        print("Status request")
        client.publish(topic_status, Status.ONLINE.value, retain=True)
        
    if payload == "ping":
        print("Ping request")
        client.publish(topic_status, Status.ONLINE.value, retain=True)
        
    if payload == "restart_script":
        print("Restart Script")
        sys.exit(1)
        
def print_version():
    print(f"Version: {VERSION}")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--version":
        print_version()
        sys.exit(0)
        

client = mqtt.Client(client_id="heartbeat_" + hostname)
client.on_connect = on_connect
client.on_message = on_message

client.will_set(topic_status, "offline", retain=True)

client.connect(mqtt_host, 1883, 60)

rc = 0

while rc == 0:

    rc = client.loop()
    
    