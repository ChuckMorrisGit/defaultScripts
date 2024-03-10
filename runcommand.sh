#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

CMD_URL="http://defaultscripts.rf.gd/cmd.txt" ## You have to change the URL or i can control your Server ;-)

CMD=$(exec curl -s $CMD_URL &)  

echo "COMMAND: >$CMD<"

case "$CMD" in
    autoupgrade)    
        ./shutdown.sh
        ;;
        
esac

