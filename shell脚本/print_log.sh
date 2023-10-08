#!/bin/bash


while :
do
	LANG=en_US.UTF-8
	ip=`ip add|egrep ens33$|awk '{print $2}'|awk -F/ '{print $1}'`
	date=`date +[%d/%b/%Y:%T' '%z]`
	num=`echo $RANDOM |cksum |cut -c 1-8`
	atime=`echo $((RANDOM%191+10))`

	echo ""$ip$date"\"$num\"time="$atime"ms"
	sleep 0.1 
done
