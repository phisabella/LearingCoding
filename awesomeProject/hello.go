package main

import (
	"fmt"
)

func varuable(){
	var a int
	var s string
	fmt.Println(a,s)
	fmt.Printf("%d %q \n",a,s)
	fmt.Printf("%d %s \n",a,s)
}

func variableInit(){
	var a,b int =3,4
	var s string = "abc"
	fmt.Println(a,b,s)
}

func variableType(){
	var a,b,c,d= 3,4,"qwe",true
	var s ="abc"
	fmt.Println(a,b,c,d,s)
}

func variableShort(){
	a :=2
	fmt.Println(a)
}

func main() {
	varuable()
	variableInit()
	variableShort()
	fmt.Println("qwe")
}
