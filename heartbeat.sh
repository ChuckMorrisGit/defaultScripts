#!/bin/bash
 
BASEDIR=$(dirname $0)
cd $BASEDIR

EXITCODE=1

while [ $EXITCODE -ne 0 ]
do
    ./heartbeat.py
    EXITCODE=$?

    bash ./updateFromGit.sh

    echo "Heartbeat exited with code $EXITCODE. Restarting in 3 seconds..."
    sleep 3
done



