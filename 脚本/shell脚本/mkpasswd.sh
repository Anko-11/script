#!/bin/bash

#定义大小字符、数字、特殊符号
upper_letter='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower_letter='abcdefghijklmnopqrstuvwxyz'
punctuation='!#$%&\()*+,-./:;<=>?@[\\]^_{|}~'
digits='0123456789'

#得到所有的位置变量，对位置变量进行判断
var_error() {
	echo "请检查你的参数是否正确，请看下面的案例"
	echo "sc_passwd usage:  sc_passwd  -l 15 -d 5 -c 3 -C 3 -s 4"
}


if  (( $# == 0 ));then
	p_len=12
	d_array=""
	for i in {1..2}
	do
		d_array+=$(( $RANDOM % ${#digits} ))
	done
	echo $d_array
		p_array+=${punctuation:$RANDOM % 31 :1}
	echo $p_array
	for i in {1..2}
	do 
		u_array+=${upper_letter:$RANDOM % 26 :1}
    done
	echo $u_array
	for i in {1..7}
	do
		l_array+=${lower_letter:$RANDOM % 26 :1}     
	done     
	echo $l_array
	echo 生成的密码 $d_array$p_array$u_array$l_array

elif ((  $# == 1 || $# == 3 || $# == 5 || $# == 7 || $# == 9 ));then
	var_error
else
	#使用循环获得所有的正确的位置变量，然后对位置变量的内容进行判断
	while getopts "l:d:c:C:s:" opt
    do
    case $opt in
    l)
        echo "选项-$opt的值是$OPTARG"
		lenth=$OPTARG
        ;;
    d)
        echo "选项-$opt的值是$OPTARG"
		d_num=$OPTARG
        ;;
    C)
        echo "选项-$opt的值是$OPTARG"
		C_num=$OPTARG
        ;;
    c)
        echo "选项-$opt的值是$OPTARG"
		c_num=$OPTARG
        ;;
    s)
        echo "选项-$opt的值是$OPTARG"
		s_num=$OPTARG
        ;;
    ?)
        echo "无效的选项 -$OPTARG"
        var_error
        exit 2
        ;;
    esac
	done
	if (( lenth < 12 ));then
		echo 密码长度必须大于12
		exit 1
	fi
	if (( lenth > 12 ));then
		echo 
fi

