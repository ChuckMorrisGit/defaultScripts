#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR


CMD=$(exec curl -s https://pool.debusson.de/cmd.txt &)

echo ">$CMD<"

case "$CMD" in
    upgrade)    
        ./shutdown.sh
        ;;
        
esac

