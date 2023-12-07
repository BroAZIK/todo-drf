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
            "info": f"{instance.id}. {instance.title} is {'completed' if instance.completed else 'incompleted'}."
        }

    def create(self, validated_data: dict) -> Task:
        return Task.objects.create(
            title=validated_data['title'],
            description=validated_data['description'],
            completed=validated_data['completed'],
        )

    def update(self,instance: Task, validated_data: dict) -> Task:
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.completed = validated_data.get('completed', instance.completed)

        instance.save()

        return instance
