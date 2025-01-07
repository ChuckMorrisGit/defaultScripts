#!/bin/bash
 
BASEDIR=$(dirname $0)
cd $BASEDIR

EXITCODE=1

while [ $EXITCODE -ne 0 ]
do
    ./heartbeat.py
    EXITCODE=$?
    sleep 3
done



