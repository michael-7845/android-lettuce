#!/bin/sh

usage() {
  echo "Usage: myconfig.sh cat|vi"
  echo "     - cat: show config using cat command"
  echo "     - vi: edit config using vi command"
  exit 0
}

if [ $# != 1 ]; then
  usage
fi

FACILITY=`cat /root/_myFacilityLocation`
BASE=`python $FACILITY/_myfacility.py -b`
CUR=`pwd`

cd "$BASE/tools"
if [ $1 = "cat" ]; then
  cat $BASE/android_lettuce.conf
elif [ $1 = "vi" ]; then
  vi $BASE/android_lettuce.conf
else
  usage
fi
cd $CUR
