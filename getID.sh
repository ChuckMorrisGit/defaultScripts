#!/bin/bash

id=`awk -F= '$1=="ID" { print $2 ;}' /etc/os-release`

echo $id
