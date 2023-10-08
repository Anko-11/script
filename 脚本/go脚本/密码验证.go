package main

import (
	"fmt"
	"strings"
)

func main()  {
	var passwd string
	fmt.Print("输入密码")
	fmt.Scan(&passwd)
	fmt.Println("密码得分为",2 + length(passwd) + cpl(passwd) + repeat(passwd))
}
//长度检查
func length(passwd string)int{
	if len(passwd) >= 8{
		return 1
	}else {
		fmt.Println("长度小于8")
		return 0
	}
}
//复杂度检查
func cpl(passwd string)int {
	var s = 0
	for _, i := range passwd {
		if strings.Contains("1234567890", string(i)) {
			s = s + 1
			break
		}
		if strings.Contains("qwertyuiopasdfghjklzxcvb", string(i)) {
			s = s + 1
			break
		}
		if strings.Contains("QWERTYUIOPASDFGHJKLZXCVBNM", string(i)) {
			s = s + 1
			break
		}
		if ! strings.Contains("1234567890qwertyuiopasdfghjklzxcvbQWERTYUIOPASDFGHJKLZXCVBNM", string(i)) {
			s = s + 1
			break
		}
	}
	if s >= 3 {
		return 1
	} else {
		fmt.Println("密码没有三种以上字符组成")
		return 0
	}
}
//重复检验
func repeat(passwd string)int{
	var a int
	for i := 0 ; i < len(passwd)-2 ; i++ {
		if strings.Contains(passwd[i+3:],passwd[i:i+3]){
			fmt.Println("密码有重复")
			a = 0
			break
		}else{
			a = 1
		}
	}
	return a
}
