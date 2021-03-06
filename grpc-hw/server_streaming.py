from __future__ import print_function

import grpc
import service_pb2_grpc as serverstreaming_pb2_grpc
import service_pb2 as serverstreaming_pb2


def make_message(message):
    return serverstreaming_pb2.Message(message=message)


def send_message(stub, num):
    responses = stub.GetServerResponse(make_message(num))
    print(f"Factoring of {num}:")
    for response in responses:
        print(f"{response.message}")


def run(arr):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = serverstreaming_pb2_grpc.ServerStreamingStub(channel)
        send_message(stub, arr)


if __name__ == '__main__':
    run(100)