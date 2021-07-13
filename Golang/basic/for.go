package main

import (
	"fmt"
)

func main() {
	strings := []string{"qwe","ao"}
	for i,is:=range strings{
		fmt.Println(i,is)
	}
	numbers := [6]int{1, 2, 3, 5}
	for i,x:= range numbers {
		fmt.Println( i,x)
	}
}
