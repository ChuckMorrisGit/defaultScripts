#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SCRIPT_NAME=`basename "$0"`


bash ./updateFromGit.sh


while getopts i flag
do
    case "${flag}" in
        i) 
            apt install curl mosquitto-clients python3-paho-mqtt 
            echo "to crontal"
            (crontab -l 2>/dev/null; echo "@reboot sleep 5m && bash $SCRIPT_DIR/$SCRIPT_NAME") | crontab -
            (crontab -l 2>/dev/null; echo "@reboot /usr/bin/screen -dmS Default") | crontab -

            rm /root/.screenrc
            echo 'caption always "%{Wb} %H %{Bk}| %{Ck}%-w%50>%{Cb} %n %t %{-}%+w%<%{- Wk}%{Bk} | %=%{Wb} %C "' > /root/.screenrc
            echo 'screen -t Heartbeat 0 sh /root/defaultScripts/heartbeat.sh' >> /root/.screenrc
            echo 'screen -t bash 1 bash' >> /root/.screenrc
            ;;
    esac
done

./runcommand.sh

