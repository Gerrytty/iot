package main

import (
    "context"
    "log"
    // "net"
    "net/http"
    "google.golang.org/grpc"
    "github.com/grpc-ecosystem/grpc-gateway/v2/runtime"
    // "google.golang.org/grpc/credentials/insecure"

)

func main() {
    addr := "localhost:9999"
    log.Printf("gateway started")
    conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())
    if err != nil {
         log.Fatal(err)
    }
    defer conn.Close()

    client := NewEchoClient(conn)
    req := MyMessage{Msg: "hello"}

    resp, err := client.SendEcho(context.Background(), &req)
    if err != nil {
         log.Fatal(err)
    }
    log.Printf("Test echo mesage: %v", resp.Msg)

    gwmux := runtime.NewServeMux()
    // Register Greeter
    err = RegisterEchoHandler(context.Background(), gwmux, conn)
    if err != nil {
        log.Fatalln("Failed to register gateway:", err)
    }

    gwServer := &http.Server{
        Addr:    ":8090",
        Handler: gwmux,
    }

    log.Println("Serving gRPC-Gateway on http://0.0.0.0:8090")
    log.Fatalln(gwServer.ListenAndServe())

}