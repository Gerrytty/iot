import math

import grpc
from concurrent import futures
import unary_pb2_grpc as pb2_grpc
import unary_pb2 as pb2


class UnaryService(pb2_grpc.RootServiceServicer):

    def __init__(self, *args, **kwargs):
        pass

    def root(self, request, context):
        message = request.number
        result = {'root': math.sqrt(message)}
        return pb2.RootResponse(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_RootServiceServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()