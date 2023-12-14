from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from datetime import datetime
from django.utils.timezone import now
from base64 import b64decode
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        if value in ['title', 'sarlavha']:
            raise serializers.ValidationError("Siz notogri title tanlagansiz.")
        return value
        

class UserSerializer(serializers.ModelSerializer):

    sorted_tasks = serializers.SerializerMethodField()

    def get_sorted_tasks(self, obj):
        # Retrieve the related objects and sort them by name
        related_objects = obj.tasks.all().order_by('-completed')

        # Serialize the sorted related objects
        serializer = TaskSerializer(related_objects, many=True)
        return serializer.data

    class Meta:
        model = User
        fields = ['id', 'username', 'sorted_tasks']
