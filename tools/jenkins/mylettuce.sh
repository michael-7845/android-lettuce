#!/bin/sh
LETTUCE_HOME="/home/ckt/lettuce"
PROJECT="lab2"
[ -n "$1" ] && PROJECT="$1"
PROJPATH="$LETTUCE_HOME/$PROJECT"

# clear log
rm -f logs/*

# run lettuce as root
sudo lettuce --with-xunit --xunit-file=./logs/lettuce_result.xml $PROJPATH/features
