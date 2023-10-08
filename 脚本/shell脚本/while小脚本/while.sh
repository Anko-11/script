#!/bin/bash

i=1
while true
do
	echo "$i"
	((i++))
	sleep 1
	if (( i == 10 ));then
		exit $i
	fi
	read -p "ENTER继续"
done


