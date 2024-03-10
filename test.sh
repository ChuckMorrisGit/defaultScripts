#!/bin/bash

id=`./helper/getID.sh`

echo $id

if grep -Fxq "$id" ./upgrade.sh
then
    echo "$id in upgrade.sh"
else
    echo "$id NOT in upgrade.sh"
fi
