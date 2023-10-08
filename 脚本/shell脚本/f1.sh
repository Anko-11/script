#!/bin/bash

#检测sshd进程
check_sshd() {
	local ssh_num=`ps aux|grep "/usr/sbin/sshd"|wc -l`
	if (($ssh_num>=2));then
		echo "sshd service is runing"
		return 0
	else
		echo "sshd service is stop"
		return 1
	fi
}

#check_sshd

#check crond
check_crond() {
	echo "sshd process number: $ssh_num"

}

#check_crond
