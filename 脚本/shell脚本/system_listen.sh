#!/bin/bash

#磁盘监听
echo "`df -Th |grep -w / |awk -F " " '{print $6}' |cut -c 1,2` > 80" |bc && echo 磁盘使用超过80% && mail -s 磁盘$0 973233548@qq.com

#内存监听
total=`free -m |grep Mem |awk -F " " '{print $2}'`
available=`free -m |grep Mem |awk -F " " '{print $7}'`
c=`echo "$total - $available" |bc` 
echo "`echo "scale=4;$c / $total" |bc` > 0.8" |bc && echo 内存使用超过80% && mail -s 内存$0 973233548@qq.com

#cpu监听
echo "`sar 1 1 |awk -F " " '{print $NF}' |tail -1` < 30" |bc && echo cpu使用超过70% && mail -s cpu$0 973233548@qq.com
