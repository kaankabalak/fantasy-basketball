package main

import (
	"fmt"
	"net/http"
)

func sayHello(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Hello world!")
}

func main() {
	fs := http.FileServer(http.Dir("../ui/build"))
	http.Handle("/", http.StripPrefix("/", fs))

	http.HandleFunc("/hello", sayHello)
	http.ListenAndServe(":8080", nil)
}
