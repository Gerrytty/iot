from concurrent import futures

import grpc
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import bidirectional_pb2


received_arr = []


class BidirectionalService(bidirectional_pb2_grpc.BidirectionalServicer):
    def GetServerResponse(self, request_iterator, context):
        for message in request_iterator:
            received_arr.append(message.message)
            yield bidirectional_pb2.Message(message=max(received_arr))
        received_arr.clear()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bidirectional_pb2_grpc.add_BidirectionalServicer_to_server(BidirectionalService(), server)
    server.add_insecure_port('[::]:8080')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()