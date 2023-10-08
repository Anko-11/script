#!/bin/bash

echo "####################"
echo "# 1.cpu使用率"
echo "# 2.内存使用疫情"
echo "# 3.磁盘/分区使用情况"
echo "# 4.退出"
echo "####################"

cpu_info() {
	ci=`sar 1 1 |awk -F " " '{print $NF}'|tail -1`
	echo "cpu已使用"$ci"%"
}
mem_info() {
	mt=`free -m |grep Mem |awk -F " " '{print $2}'`
	mi=`free -m |grep Mem |awk -F " " '{print $4}'`
	echo "总量"$mt"M 空闲"$mi"M"
}
disk_info() {
	dt=`df -Th |grep -w / |awk -F " " '{print $3}'`
	di=`df -Th |grep -w / |awk -F " " '{print $6}'`
	echo "总量$dt 已使用$di"
}


while :
do
	read -p "输入：" sl
	case $sl in
	1)
		cpu_info
		;;
	2)
		mem_info
		;;	
	3)
		disk_info
		;;
	4)
		exit 0
		;;
	esac
done
