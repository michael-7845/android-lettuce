#!/bin/sh

if [ -n "$1" ]; then
PROJECT="$1"
else
echo "Usage: update_project.sh <project>"
exit 0
fi

FACILITY=`cat /root/_myFacilityLocation`
BASE=`python $FACILITY/_myfacility.py -b`
CUR=`pwd`

cd "$BASE/tools"
./svnlettuce.py -t
./svnlettuce.py -m
./svnlettuce.py -u $PROJECT
cd $CUR
