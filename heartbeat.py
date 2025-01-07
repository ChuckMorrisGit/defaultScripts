#!/usr/bin/env python3

# afutros720_runlevel

import paho.mqtt.client as mqtt
import os
hostname = os.uname()[1]

mqtt_host="192.168.2.70"

topic_status = "devices/" + hostname + "/status"
topic_runlevel = "devices/" + hostname + "/runlevel"
runLevel = ""

def setRunLevel(runlevel):
    global runLevel
    
    runLevel = runlevel
    client.publish(topic_runlevel, runLevel, retain=True)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("devices/" + hostname + "/cmd")
    client.publish(topic_status, "online", retain=True)
    setRunLevel("running")
    

def on_message(client, userdata, msg):
    payload = str(msg.payload.decode('ascii'))
    
    if payload == "reboot":
        print("Rebooting")
        client.publish(topic_status, "rebooting", retain=True)
        setRunLevel("rebooting")
        os.system("./reboot.sh &")
        
    if payload == "shutdown":    
        print("Shutting down")
        client.publish(topic_status, "shutting down", retain=True)
        setRunLevel("shutting down")
        os.system("./shutdown.sh &")
    
    if payload == "status":
        print("Status request")
        client.publish(topic_status, "online", retain=True)
        
    if payload == "ping":
        print("Ping request")
        client.publish(topic_status, "online", retain=True)
        
    if payload == "update":
        print("Update request")
        client.publish(topic_status, "updating", retain=True)
        setRunLevel("updating")
        os.system("./upgrade.sh &")
        


client = mqtt.Client(client_id="heartbeat_" + hostname)
client.on_connect = on_connect
client.on_message = on_message

client.will_set(topic_status, "offline", retain=True)

client.connect(mqtt_host, 1883, 60)

rc = 0


while rc == 0:

    rc = client.loop()