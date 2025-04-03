from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # Optional: Custom edit (PATCH) method if you need extra logic
    @action(detail=True, methods=['patch'])
    def mark_completed(self, request, pk=None):
        todo = self.get_object()
        todo.completed = True
        todo.save()
        return Response(self.get_serializer(todo).data)

    # Optional: Custom delete (DELETE) method
    @action(detail=True, methods=['delete'])
    def delete_task(self, request, pk=None):
        todo = self.get_object()
        todo.delete()
        return Response({"message": "Task deleted successfully"}, status=204)
