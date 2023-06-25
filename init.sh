#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
SCRIPT_NAME=`basename "$0"`

git stash
git pull

chmod -R +x *.sh

while getopts i flag
do
    case "${flag}" in
        i) 
            echo "to crontal"
            (crontab -l 2>/dev/null; echo "@reboot bash $SCRIPT_DIR/$SCRIPT_NAME") | crontab -
            ;;
    esac
done

./runcommand.sh

