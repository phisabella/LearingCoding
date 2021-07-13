package main

import "fmt"

func main() {
	a:=10
	fmt.Println(&a)

	b:=20
	ip:=&b
	fmt.Println(ip)
	fmt.Println(*ip)

}
