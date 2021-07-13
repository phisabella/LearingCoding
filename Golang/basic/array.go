package main

import "fmt"

func main() {
	//var balaance = [5]float32{1000,123,123,123,123}
	//ba:=[5]float32{123,123,123,123}
	//baa:=[...]float32{123123123}
	//baaa:=[5]float32{1:2,3:7.0}
	//for i:=0;i<5;i++{
	//	fmt.Println(balaance[i])
	//	fmt.Println(ba[i])
	//	fmt.Println(baa[i])
	//	fmt.Println(baaa[i])
	//}

	//Multidimensional array
	values := [][]int{}
	row1:=[]int{1,2,3}
	row2:=[]int{3,2,1}
	values = append(values,row2)
	values = append(values,row1)
	fmt.Println(values[0])
	fmt.Println(values[1])

	fmt.Println(values[0][0])

	a:=[3][4]int{
		{0,1,2,3},
		{4,1,1,1},
		{1,2,3,2},
	}
	fmt.Println(a)
}
