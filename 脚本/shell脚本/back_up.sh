#!/bin/bash

if (( $# > 1 ));then
	if [[ $1 == '-rf' ]];then
		[ -e $2 ] && mv $2 /root/lianxi/5.19/backup || echo "$2 不存在"
	fi
else
	mv $1 /root/lianxi/5.19/backup
	
fi

#if [ -e $1 ];then
#	mv $1 /root/lianxi/5.19/backup
#else
#	echo "$1 不存在"
#fi
