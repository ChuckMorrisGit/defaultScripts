#!/bin/bash
 
BASEDIR=$(dirname $0)
cd $BASEDIR

EXITCODE=1

#while [ $EXITCODE -ne 0 ]
while [ true ]
do
    ./heartbeat.py
    EXITCODE=$?

    echo "Heartbeat exited with code $EXITCODE. Restarting in 3 seconds..."
    sleep 3

    bash ./updateFromGit.sh

done



