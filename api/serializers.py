from rest_framework import serializers
from .models import Task
from datetime import datetime


class TaskSerializer(serializers.Serializer):
    id          = serializers.IntegerField(read_only=True)
    title       = serializers.CharField(max_length=200)
    completed   = serializers.BooleanField(default=False)
    description = serializers.CharField(default='', allow_blank=True)
    created     = serializers.DateTimeField(default=datetime.now)

    def to_representation(self, instance: Task) -> dict:
        return {
            "info": f"{instance.id} {instance.title} is {'completed' if instance.completed else 'incompleted'}."
        }

