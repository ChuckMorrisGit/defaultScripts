#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

SCRIPT_PATH=$( basename -- "$0"; ), dirname $( dirname -- "$0"; )

#git pull

chmod +x *.sh

echo $SCRIPT_PATH

while getopts i flag
do
    case "${flag}" in
        u) echo "to crontal";;
    esac
done

