package main

import (

	"encoding/json"
	"fmt"
	"io/ioutil"
	"math/rand"
	"os"
	"time"
)
func main()  {
	var p string
	count := map[string]int{}
	name := []string{"赵","钱","孙","李","王","刘"}
	c, _ := ioutil.ReadFile("database.txt")
	json.Unmarshal(c, &count)
	for {
		if len(name) == 0 {
			fmt.Print("全部已经抽到")
			break
		}else{
			fmt.Print("输入任意键继续，q退出，r清零：")
			fmt.Scanln(&p)
			if p == "q" {
				fmt.Printf("结束")
				break
			}else if p == "r"{
				fmt.Printf("所有学生点名次数以清空")
				count = map[string]int{"赵":0, "钱":0, "孙":0, "李":0, "王":0, "刘":0}
				break
			}
			a := random(0, len(name))
			fmt.Println(name[a])
			count[name[a]] += 1
			fmt.Println(count)
			name = append(name[:a], name[a+1:]... )
		}
	}
	//写入文件
	file, _ := os.Create("database.txt")
	data, _ := json.Marshal(count)
	file.Write(data)
	defer file.Close()
}
func random(min, max int) int {
	rand.Seed(time.Now().Unix())
	return rand.Intn(max - min) + min
}

