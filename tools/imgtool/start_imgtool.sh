#!/bin/sh
FACILITY=`cat /root/_myFacilityLocation`
BASE=`python $FACILITY/_myfacility.py -b`
CUR=`pwd`
java -jar "$BASE/tools/imgtool/imgtool.jar"

