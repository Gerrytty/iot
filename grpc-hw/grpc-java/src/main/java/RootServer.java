import grpcgenerated.RootServiceImpl;
import io.grpc.Server;
import io.grpc.ServerBuilder;

import java.io.IOException;

public class RootServer {
    public static void main(String[] args) throws IOException, InterruptedException {
        Server server = ServerBuilder.forPort(8080).addService(new RootServiceImpl()).build();
        server.start();
        server.awaitTermination();
    }
}