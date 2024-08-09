#!/bin/bash

systemctl stop openhab.service

echo y | openhab-cli clean-cache

echo y | openhab-cli reset-ownership

rm /var/lib/openhab/jsondb/*.marketplace.*

./reboot.sh
