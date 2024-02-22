# py-grpc
It contains basic implementation of grpc in Python. We have a client and server which are communicating through grpc

# To create proto descriptor file
python -m grpc_tools.protoc -I./ --python_out=. --pyi_out=. --grpc_python_out=. ./name.proto
