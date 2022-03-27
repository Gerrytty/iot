import grpcgenerated.RootRequest;
import grpcgenerated.RootResponse;
import grpcgenerated.RootServiceGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

public class GrpcClient {


    public static double sendRequest(int number) {
        ManagedChannel channel =
                ManagedChannelBuilder.forAddress("localhost", 8080)
                .usePlaintext()
                .build();

        RootServiceGrpc.RootServiceBlockingStub stub = RootServiceGrpc.newBlockingStub(channel);

        RootRequest rootRequest = RootRequest.newBuilder()
                .setNumber(number)
                .build();

        RootResponse rootResponse = stub.root(rootRequest);

        channel.shutdown();

        return rootResponse.getRoot();
    }


    public static void main(String[] args) {
        double resp = sendRequest(100);
        System.out.println(resp);
    }
}