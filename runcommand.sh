#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

CMD_URL="https://raw.githubusercontent.com/ChuckMorrisGit/defaultScripts/main/command.txt" ## You have to change the URL or i can control your Server ;-)

CMD=$(exec curl -s $CMD_URL &)  

echo "COMMAND: >$CMD<"

case "$CMD" in
    autoupgrade)    
        ./shutdown.sh
        ;;
        
esac

