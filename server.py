import grpc
from concurrent import futures
import todo_pb2_grpc
from service import TodoService


def serve():
      
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    todo_pb2_grpc.add_TodoServicer_to_server(TodoService(), server)
    server.add_insecure_port('[::]:40000')
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()