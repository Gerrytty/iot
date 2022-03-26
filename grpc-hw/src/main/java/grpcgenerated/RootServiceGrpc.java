package grpcgenerated;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.27.2)",
    comments = "Source: simple.proto")
public final class RootServiceGrpc {

  private RootServiceGrpc() {}

  public static final String SERVICE_NAME = "RootService";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<RootRequest,
      RootResponse> getRootMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "root",
      requestType = RootRequest.class,
      responseType = RootResponse.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<RootRequest,
      RootResponse> getRootMethod() {
    io.grpc.MethodDescriptor<RootRequest, RootResponse> getRootMethod;
    if ((getRootMethod = RootServiceGrpc.getRootMethod) == null) {
      synchronized (RootServiceGrpc.class) {
        if ((getRootMethod = RootServiceGrpc.getRootMethod) == null) {
          RootServiceGrpc.getRootMethod = getRootMethod =
              io.grpc.MethodDescriptor.<RootRequest, RootResponse>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "root"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  RootRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  RootResponse.getDefaultInstance()))
              .setSchemaDescriptor(new RootServiceMethodDescriptorSupplier("root"))
              .build();
        }
      }
    }
    return getRootMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static RootServiceStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<RootServiceStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<RootServiceStub>() {
        @java.lang.Override
        public RootServiceStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new RootServiceStub(channel, callOptions);
        }
      };
    return RootServiceStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static RootServiceBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<RootServiceBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<RootServiceBlockingStub>() {
        @java.lang.Override
        public RootServiceBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new RootServiceBlockingStub(channel, callOptions);
        }
      };
    return RootServiceBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static RootServiceFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<RootServiceFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<RootServiceFutureStub>() {
        @java.lang.Override
        public RootServiceFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new RootServiceFutureStub(channel, callOptions);
        }
      };
    return RootServiceFutureStub.newStub(factory, channel);
  }

  /**
   */
  public static abstract class RootServiceImplBase implements io.grpc.BindableService {

    /**
     */
    public void root(RootRequest request,
        io.grpc.stub.StreamObserver<RootResponse> responseObserver) {
      asyncUnimplementedUnaryCall(getRootMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getRootMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                RootRequest,
                RootResponse>(
                  this, METHODID_ROOT)))
          .build();
    }
  }

  /**
   */
  public static final class RootServiceStub extends io.grpc.stub.AbstractAsyncStub<RootServiceStub> {
    private RootServiceStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected RootServiceStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new RootServiceStub(channel, callOptions);
    }

    /**
     */
    public void root(RootRequest request,
        io.grpc.stub.StreamObserver<RootResponse> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getRootMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class RootServiceBlockingStub extends io.grpc.stub.AbstractBlockingStub<RootServiceBlockingStub> {
    private RootServiceBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected RootServiceBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new RootServiceBlockingStub(channel, callOptions);
    }

    /**
     */
    public RootResponse root(RootRequest request) {
      return blockingUnaryCall(
          getChannel(), getRootMethod(), getCallOptions(), request);
    }
  }

  /**
   */
  public static final class RootServiceFutureStub extends io.grpc.stub.AbstractFutureStub<RootServiceFutureStub> {
    private RootServiceFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected RootServiceFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new RootServiceFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<RootResponse> root(
        RootRequest request) {
      return futureUnaryCall(
          getChannel().newCall(getRootMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_ROOT = 0;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final RootServiceImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(RootServiceImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_ROOT:
          serviceImpl.root((RootRequest) request,
              (io.grpc.stub.StreamObserver<RootResponse>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class RootServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    RootServiceBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return Simple.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("RootService");
    }
  }

  private static final class RootServiceFileDescriptorSupplier
      extends RootServiceBaseDescriptorSupplier {
    RootServiceFileDescriptorSupplier() {}
  }

  private static final class RootServiceMethodDescriptorSupplier
      extends RootServiceBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    RootServiceMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (RootServiceGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new RootServiceFileDescriptorSupplier())
              .addMethod(getRootMethod())
              .build();
        }
      }
    }
    return result;
  }
}
