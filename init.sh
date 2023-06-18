#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )

#git pull

chmod +x *.sh

echo $SCRIPT_DIR

while getopts i flag
do
    case "${flag}" in
        i) echo "to crontal";;
    esac
done

