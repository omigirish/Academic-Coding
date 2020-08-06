#!/bin/bash
now=`date +%d\/%m\/%Y`
echo -n "Current system date is: "
echo "$now"
data=`who`

echo "The following users are currently logged into the system: "
echo "`who`"
