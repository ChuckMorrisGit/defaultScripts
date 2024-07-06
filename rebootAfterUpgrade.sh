#!/bin/bash

systemctl stop openhab.service

openhab-cli clean-cache

openhab-cli reset-ownership

rm /var/lib/openhab/jsondb/*.marketplace.*

./reboot.sh
