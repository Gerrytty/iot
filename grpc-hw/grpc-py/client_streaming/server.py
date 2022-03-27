from concurrent import futures

import grpc
import clientstreaming_pb2_grpc
import clientstreaming_pb2

import numpy as np


received_arr = []


class BidirectionalService(clientstreaming_pb2_grpc.ClientStreamingServicer):
    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            received_arr.append(message.message)
        result = {'message': np.std(received_arr)}
        received_arr.clear()
        return clientstreaming_pb2.Message(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    clientstreaming_pb2_grpc.add_ClientStreamingServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()