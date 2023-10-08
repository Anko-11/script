#!/bin/bash

#此脚本用于游戏，玩家猜唐僧的紫金钵钵价格

#随机紫金钵钵价格
price=$(( $RANDOM % 101 ))
#猜的次数
i=1

while :
do
	echo "唐僧的紫金钵钵价格是:"
	#玩家猜的价格
	read p_price
	if (( $p_price == $price )) && (( $i == 1 )) ;then
		echo you are rulai	
		exit 0
	elif (( $p_price == $price )) && (( 2 <= $i <=5 ));then
        echo you are wukong
        exit 0
	elif (( $p_price == $price )) && (( $i > 10 ));then
        echo you are bajie
        exit 0
	else
		echo "唐僧的紫金钵钵价格不是$p_price"
	fi
#次数加一
	let i=i+1
done
