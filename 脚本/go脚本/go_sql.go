package main

import (
	"database/sql"
	"fmt"
	_ "github.com/go-sql-driver/mysql"
	"log"
)

func main() {
	// 设置连接数据库的参数
	//"用户名:密码@[连接方式](主机名:端口号)/数据库名"
	db,_ := sql.Open("mysql", "sc:sc123789@tcp(192.168.17.130:3306)/sc")
	defer db.Close()    //关闭数据库
	err:=db.Ping()      //连接数据库
	if err!=nil{
		fmt.Println("数据库连接失败")
		return
	}
	fmt.Println("连接数据库成功~")

	// 使用 "Query" 方法可以执行查询并返回结果集。然后使用 "Scan" 方法从结果集中获取每一行的数据。
	rows, _ := db.Query("SELECT * FROM StuInfo")
	defer rows.Close()
	for rows.Next() {
		var id int
		var age int
		var name string
		var address string
		if err := rows.Scan(&id, &name, &age, &address); err != nil {
			log.Fatal(err)
		}
		fmt.Printf("ID: %d, AGE: %d, Name: %s, ADDRESS: %s\n", id, age, name, address)
	}
}