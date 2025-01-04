#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SCRIPT_NAME=`basename "$0"`

git stash
git pull

chmod +x *.sh
chmod +x *.py
chmod +x ./helper/*.sh

while getopts i flag
do
    case "${flag}" in
        i) 
            apt install curl mosquitto-clients python3-paho-mqtt
            echo "to crontal"
            (crontab -l 2>/dev/null; echo "@reboot sleep 5m && bash $SCRIPT_DIR/$SCRIPT_NAME") | crontab -
            ;;
    esac
done

./runcommand.sh

