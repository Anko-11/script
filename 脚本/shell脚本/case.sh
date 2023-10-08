#!/bin/bash

#case练习

case $1 in
start)
	echo "start scweb"
	mkdir start$RANDOM
	;;
stop)
	echo "stop scweb"
	mkdir stop$RANDOM
	;;
restart|reload|re)
	echo "restart scweb"
	;;
*)
	echo "please input start/stop/restart"
	;;
esac
