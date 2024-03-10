#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

id=`./helper/getID.sh`

case "$id" in

    opensuse|opensuse-tumbleweed)
        zypper up
        ;;

    fedora)
        dnf upgrade --refresh
        ;;

    *)
        sudo apt update
        sudo apt -y upgrade
        sudo apt -y autoremove
        ;;

esac
  

