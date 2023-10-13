package main

import "fmt"

type Stuinfo struct {
	Id int
	Name string
	Age int
	Address string
}

//创建学生信息
func ad(student map[int]Stuinfo){
	var id int
	var name string
	var age int
	var address string
	fmt.Println("输入id，name，age，adress 以空格分割")
	fmt.Scanln(&id, &name, &age, &address)
	StuInfo := Stuinfo{
		Id: id,
		Name: name,
		Age: age,
		Address: address,
	}
	student[id] = StuInfo
	fmt.Println("已录入学生信息")
	fmt.Printf("%+v\n", StuInfo)
}

//修改学生信息
func ch(student map[int]Stuinfo){
	fmt.Println("输入你要修改的学生id")
	var id int
	var flag int
	fmt.Scanln(&id)
	for i, _ := range student{
		if i == id{
			ad(student)
			flag = 1
			break
		}
		if i != id{
			flag = 0
		}
	}
	if flag == 0{
		fmt.Println("输入id不存在")
	}
}

//删除学生信息
func de(student map[int]Stuinfo){
	fmt.Println("输入你要删除的学生id")
	var id int
	var flag int
	fmt.Scanln(&id)
	for i, _ := range student{
		if i == id{
			delete(student, id)
			fmt.Println("已删除学生信息")
			flag = 1
			break
		}
		if i != id{
			flag = 0
		}
	}
	if flag == 0{
		fmt.Println("输入id不存在")
	}
}

//查询学生信息
func lp(student map[int]Stuinfo){
	if len(student) == 0{
		fmt.Println("暂时没有学生信息")
	}else {
		fmt.Println("id   name   age   address")

		for i, j := range student{
			fmt.Printf("%-5d",i)
			fmt.Printf("%-5s",j.Name)
			fmt.Printf("%-5d",j.Age)
			fmt.Printf("%-5s\n",j.Address)
		}
	}
}

func main()  {
	var student map[int]Stuinfo
	student = make(map[int]Stuinfo)
	var c int
	for c != 5{
		fmt.Println("输入选项1-5\n创建，修改，删除，查询，退出")
		fmt.Scanln(&c)
		if c == 1{
			ad(student)
		}
		if c == 2{
			ch(student)
		}
		if c == 3 {
			de(student)
		}
		if c == 4 {
			lp(student)
		}
	}
}
