from setuptools import setup, find_packages

setup(
    name="grpc_client_poc",
    version="0.1",
    packages=find_packages(),
    install_requires=["grpcio", "grpcio-tools", "protobuf"],
    include_package_data=True,
    description="gRPC client module",
)
