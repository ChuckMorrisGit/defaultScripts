#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR


./upgrade.sh

/sbin/reboot
