#!/bin/bash

for i in `seq $2`
do
	if useradd $1$i &>/dev/null ;then
		echo "新建用户 $1$i"
		passwd=`mkpasswd -l 15`
		echo "密码：$passwd"
		echo "$passwd"|passwd $1$i --stdin
		echo "用户名$1$i 密码 $passwd" >>user_passwd.txt
	else
		echo "$1$i 用户存在" 
	fi
done
