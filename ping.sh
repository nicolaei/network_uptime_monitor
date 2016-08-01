#!/bin/bash
TARGET=$1 # Target IP address
COUNT=3 # Amount of pings
TIMEOUT=1 # Timeout in seconds
LOCATION="/home/admin/logs/ping/$2" # Output location

DATE="$(date +'%Y-%m-%d %H:%M')"
PING="$(ping -c $COUNT -W $TIMEOUT $TARGET)"
# ping has a exit code of 0 if it is sucessful
if [ $? -eq 0 ]; then
    # Get min/avg/max from ping output
    PING="$(echo $PING | awk '{print $(NF-1)}' | cut -d '/' -f 1,2,3)"
else
    # If the host is not avaliable we just have -1
    PING="-1/-1/-1"
fi

# Output to file
echo "${DATE} ${PING}" >> $LOCATION
