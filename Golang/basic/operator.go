package main

import "fmt"

func main() {
	var a int = 21
	var b int = 23
	var c int

	c = a + b
	fmt.Printf("%d\n",c)
	c = a /b
	fmt.Printf("%d\n",c)
	c = a %b
	fmt.Printf("%d\n",c)

	//d:=2
	//e:="2"

	//if( d == e ) {
	//	fmt.Printf("第一行 - a 等于 b\n" )
	//} else {
	//	fmt.Printf("第一行 - a 不等于 b\n" )
	//}

	//位运算符
	q:= 60
	p:=13
	r:=0
	var ptr = &q

	r = q & p
	fmt.Printf("第一行 - r 的值为 %d\n", r )
	fmt.Println(q<<2)
	fmt.Println(&q)
	fmt.Println(ptr)
}
