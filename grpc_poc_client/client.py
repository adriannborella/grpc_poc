import grpc
from grpc_poc_client import calculator_pb2
from grpc_poc_client import calculator_pb2_grpc


def sumFunction(num1, num2):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = calculator_pb2_grpc.CalculatorStub(channel)
        response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
    print(f"Result: {response.result}")


class GrpcPocClient:
    def __init__(self, host, port):
        self._host = host
        self._port = port

    def sumFunction(self, num1, num2):
        with grpc.insecure_channel(f"{self._host}:{self._port}") as channel:
            stub = calculator_pb2_grpc.CalculatorStub(channel)
            response = stub.Add(calculator_pb2.AddRequest(num1=num1, num2=num2))
            return response


if __name__ == "__main__":
    # Get user Input
    num1 = int(input("Please input num1: "))
    num2 = int(input("Please input num2: "))
    sumFunction(num1, num2)
