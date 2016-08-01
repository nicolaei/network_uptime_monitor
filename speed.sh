#!/bin/bash
TARGET=$1 # Target IP address
LOCATION="/home/admin/logs/speed/$2" # Output location
TMP_LOG="/tmp/speedtest_tmp_log.txt"

DATE="$(date +'%Y-%m-%d %H:%M')"

wget -o $TMP_LOG -O /dev/null $TARGET

if [ $? -eq 0 ]; then
    AVERAGE=$(tail -n 2 $TMP_LOG | grep -o "(.*)" | tr -d '(' | tr -d ') MB/s')
    TIME=$(tail -n 4 $TMP_LOG | grep "100%" | grep -o "=.*s" | tr -d '=' | tr -d 's')
else
    # If the host is not avaliable we just have -1
    AVERAGE="-1"
    TIME="-1"
fi

# Output to file
echo "${DATE} ${AVERAGE}/${TIME}" >> $LOCATION
