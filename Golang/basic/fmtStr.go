package main

import "fmt"

func main() {
	var stockcode=123
	var endate="2020-12-31"
	var url = "code=%d&endDate=%s"
	var target_url=fmt.Sprintf(url,stockcode,endate)
	fmt.Println(target_url)
}
