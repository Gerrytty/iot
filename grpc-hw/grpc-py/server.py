from concurrent import futures

import grpc
import service_pb2_grpc
import service_pb2

import numpy as np
import math


received_arr_max = []
received_arr_std = []


def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(n)
   return primfac


class BidirectionalService(service_pb2_grpc.BidirectionalServicer):
    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            received_arr_max.append(message.message)
            yield service_pb2.Message(message=max(received_arr_max))
        received_arr_max.clear()


class ClientStreamingService(service_pb2_grpc.ClientStreamingServicer):
    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            received_arr_std.append(message.message)
        result = {'message': np.std(received_arr_std)}
        received_arr_std.clear()
        return service_pb2.Message(**result)


class ServerStreamingService(service_pb2_grpc.ServerStreamingServicer):
    def GetServerResponse(self, request, context):
        response = primfacs(request.message)
        for message in response:
            yield service_pb2.Message(message=message)


class UnaryService(service_pb2_grpc.UnaryServicer):

    def __init__(self, *args, **kwargs):
        pass

    def GetServerResponse(self, request, context):
        message = request.message
        result = {'message': math.sqrt(message)}
        return service_pb2.Message(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    service_pb2_grpc.add_ClientStreamingServicer_to_server(ClientStreamingService(), server)
    service_pb2_grpc.add_ServerStreamingServicer_to_server(ServerStreamingService(), server)
    service_pb2_grpc.add_UnaryServicer_to_server(UnaryService(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()