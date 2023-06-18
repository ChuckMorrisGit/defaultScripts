#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

SCRIPT_PATH=$0

git pull

chmod +x *.sh

echo $SCRIPT_PATH



