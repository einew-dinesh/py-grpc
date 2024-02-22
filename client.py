import grpc
import todo_pb2
import todo_pb2_grpc
import sys

def run():
    channel = grpc.insecure_channel('localhost:40000')
    stub = todo_pb2_grpc.TodoStub(channel)

    text = sys.argv[1]
    print(text)

    response = stub.createTodo(todo_pb2.TodoItem(id=-1, text=text))
    print("Received from server: " + str(response))

    # Uncomment below if you want to read todos synchronously
    # response = stub.readTodos(todo_pb2.voidNoParam())
    # print("Received todos from server: " + str(response))

    # Streaming readTodos
    # call = stub.readTodosStream(todo_pb2.voidNoParam())
    # for item in call:
    #     print("Received item from server: " + str(item))

if __name__ == '__main__':
    run()
