#!/bin/bash

#定义扫描端口号
port=22
ip=8.219.110.232
ctime=$(date +%Y%m%d%H%M%S)
#扫描特定ip地址的服务器端口
if  nc -w 1 -z $ip $port ;then
	echo "$ctime $ip server sshd service is running"|tee -a ${ip}_sshd.log
else
	echo "$ctime $ip server sshd service is stop"|tee -a ${ip}_sshd.log
fi

