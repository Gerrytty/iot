from __future__ import print_function

import grpc
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import bidirectional_pb2 as bidirectional_pb2

def make_message(message):
    return bidirectional_pb2.Message(message=message)


def generate_messages(number_array):
    for number in number_array:
        yield make_message(number)


def send_message(stub, arr):
    responses = stub.GetServerResponse(generate_messages(arr))
    for response in responses:
        print(f"New maximum in array {response.message}")


def run(arr):
    with grpc.insecure_channel('localhost:8080') as channel:
        stub = bidirectional_pb2_grpc.BidirectionalStub(channel)
        send_message(stub, arr)


if __name__ == '__main__':
    run([1, 2, 0, 10, 5])