#!/usr/bin/env python3

# afutros720_runlevel

import paho.mqtt.client as mqtt
import os
from enum import Enum
import sys
import subprocess
import argparse

def get_commit_count():
    try:
        count = subprocess.check_output(["git", "rev-list", "--count", "HEAD"]).strip().decode('utf-8')
        return count
    except Exception as e:
        return "Unknown"
    
VERSION = "1.0." + str(get_commit_count())

verbose = False

### MQTT Section ###
hostname = os.uname()[1]

mqtt_host="192.168.2.70"

topic_status = "devices/" + hostname + "/status"
topic_runlevel = "devices/" + hostname + "/runlevel"
topic_version = "devices/" + hostname + "/version"

runLevel = ""
### END MQTT Section ###


class Status(Enum):
    ONLINE = "online"
    OFFLINE = "offline"
    RUNNING = "running"
    STOPPED = "stopped"
    REBOOTING = "rebooting"
    SHUTTING_DOWN = "shutting down"
    UPDATING = "updating"
    ERROR = "error"
    UNKNOWN = "unknown"


def setRunLevel(runlevel):
    global runLevel
    
    runLevel = runlevel
    client.publish(topic_runlevel, runLevel, retain=True)


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("devices/" + hostname + "/cmd")
    client.subscribe("devices/all/cmd")
    client.publish(topic_status, Status.ONLINE.value, retain=True)
    client.publish(topic_version, VERSION, retain=True)
    setRunLevel(Status.RUNNING.value)


def on_message(client, userdata, msg):
    payload = str(msg.payload.decode('ascii'))
    
    if runLevel == Status.RUNNING.value:
        setRunLevel(Status.UNKNOWN.value)
        
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



## MAIN PROGRAM ##

client = mqtt.Client(client_id="heartbeat_" + hostname)
client.on_connect = on_connect
client.on_message = on_message

client.will_set(topic_status, "offline", retain=True)

client.connect(mqtt_host, 1883, 60)
       
parser = argparse.ArgumentParser()
parser.add_argument("-v", "--verbosity", help="increase output verbosity", action="store_true")
parser.add_argument("--version", help="show Version", action="store_true")
parser.add_argument("--set_runlevel", help="Set Runlevel from Extern script", action="store")

args = parser.parse_args()
if args.verbosity:
    verbose = True

if args.version:
    print(f"Version: {VERSION}")
    sys.exit(0)
    
if args.set_runlevel:
    setRunLevel(args.set_runlevel)
    sys.exit(0)
    

rc = 0

while rc == 0:

    rc = client.loop()
    
    