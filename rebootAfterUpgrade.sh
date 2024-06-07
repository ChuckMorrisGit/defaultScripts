#!/bin/bash

openhab-cli clean-cache

openhab-cli reset-ownership

./reboot.sh
