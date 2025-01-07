#!/bin/bash

BASEDIR=$(dirname $0)
cd $BASEDIR

git stash
git pull

chmod +x *.sh
chmod +x *.py
chmod +x ./helper/*.sh

