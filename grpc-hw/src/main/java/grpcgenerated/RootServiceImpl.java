package grpcgenerated;

import io.grpc.stub.StreamObserver;
import java.lang.*;

public class RootServiceImpl extends RootServiceGrpc.RootServiceImplBase {

    @Override
    public void root(RootRequest request, StreamObserver<RootResponse> responseObserver) {

        double result = Math.sqrt(request.getNumber());

        RootResponse response = RootResponse.newBuilder().setRoot(result).build();

        responseObserver.onNext(response);
        responseObserver.onCompleted();
    }
}
