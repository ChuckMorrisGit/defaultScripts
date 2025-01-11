#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

./upgrade.sh


./heartbeat.sh --set_runlevel "init 0"

init 0

