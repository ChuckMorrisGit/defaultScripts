#!/bin/bash

systemctl stop openhab.service

openhab-cli clean-cache

openhab-cli reset-ownership

./reboot.sh
