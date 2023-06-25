#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR


CMD=$(exec curl -s https://defaultscripts.rf.gd/cmd.txt &)  ## You have to change the URL or i can control your Server ;-)

echo "COMMAND: >$CMD<"

case "$CMD" in
    autoupgrade)    
        ./shutdown.sh
        ;;
        
esac

