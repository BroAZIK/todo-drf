from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Task

from .serializers import TaskSerializer


class TaskView(APIView):
    def get(self, request: Request) -> Response:
        tasks = Task.objects.all()

        serializer = TaskSerializer(tasks, many=True)
        
        return Response(serializer.data)
        