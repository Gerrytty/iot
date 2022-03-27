from __future__ import print_function

import grpc
import service_pb2_grpc as clientstreaming_pb2_grpc
import service_pb2 as clientstreaming_pb2


def make_message(message):
    return clientstreaming_pb2.Message(message=message)


def generate_messages(number_array):
    for number in number_array:
        yield make_message(number)


def send_message(stub, arr):
    response = stub.GetServerResponse(generate_messages(arr))
    print(f"STD of {arr} = {response.message}")


def run(arr):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = clientstreaming_pb2_grpc.ClientStreamingStub(channel)
        send_message(stub, arr)


if __name__ == '__main__':
    run([1, 2, 0, 10, 5])