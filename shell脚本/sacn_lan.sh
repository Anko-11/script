#!/bin/bash

#clear file
> ip_used.txt
> un_unused.txt

# ping localhost
for i in {1..254}
do
    (if ping -c 1 -w 1  172.24.89.$i &>>/dev/null ;then
		echo 172.24.89.$i is used |tee -a ip_used.txt
	else
		echo 172.24.89 $i is not used |tee -a ip_unused.txt
	fi)&
done
wait

num1=`wc -l < ip_used.txt`
num2=`wc -l < ip_unused.txt`

echo 已使用的ip地址有$num1 个
echo 未使用的ip地址有$num2 个
