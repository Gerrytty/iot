from concurrent import futures

import grpc
import serverstreaming_pb2_grpc
import serverstreaming_pb2


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


class BidirectionalService(serverstreaming_pb2_grpc.ServerStreamingServicer):
    def GetServerResponse(self, request, context):
        response = primfacs(request.message)
        for message in response:
            yield serverstreaming_pb2.Message(message=message)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    serverstreaming_pb2_grpc.add_ServerStreamingServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()