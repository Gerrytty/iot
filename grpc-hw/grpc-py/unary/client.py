import grpc
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class RootClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8080
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = pb2_grpc.RootServiceStub(self.channel)

    def get_root(self, num):
        message = pb2.RootRequest(number=num)
        return self.stub.root(message)


if __name__ == '__main__':
    client = RootClient()
    result = client.get_root(100)
    print(f'{result}')