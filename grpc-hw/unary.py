import grpc
import service_pb2_grpc as pb2_grpc
import service_pb2 as pb2


class RootClient(object):
    def __init__(self):
        self.host = 'localhost'
        self.server_port = 8080
        self.channel = grpc.insecure_channel(f"{self.host}:{self.server_port}")
        self.stub = pb2_grpc.UnaryStub(self.channel)

    def get_root(self, num):
        message = pb2.Message(message=num)
        response = self.stub.GetServerResponse(message)
        print(f"Root of {num} = {response.message}")
        return response


if __name__ == '__main__':
    client = RootClient()
    result = client.get_root(100)