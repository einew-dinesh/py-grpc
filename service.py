import todo_pb2_grpc
import todo_pb2

class TodoService(todo_pb2_grpc.TodoServicer):
    def __init__(self):
        self.todos = []

    def createTodo(self, request, context):
        todo_item = {
            "id": len(self.todos) + 1,
            "text": request.text
        }
        self.todos.append(todo_item)
        return todo_pb2.TodoItem(id=todo_item["id"], text=todo_item["text"])

    def readTodosStream(self, request, context):
        for todo_item in self.todos:
            yield todo_pb2.TodoItem(id=todo_item["id"], text=todo_item["text"])

    def readTodos(self, request, context):
        return todo_pb2.TodoItems(items=[todo_pb2.TodoItem(id=item["id"], text=item["text"]) for item in self.todos])
