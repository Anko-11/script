#!/bin/bash

num=$(ps aux|grep "/usr/sbin/sshd"|wc -l)

ctime=$(date %Y%m%d%H%M%S)
#记录到日志文件

if (( $num >= 2 ));then
	echo "sshd deamon is running" > sshd_monitor.log
else
	echo "sshd deamon is stop"
fi
