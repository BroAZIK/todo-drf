from rest_framework import serializers
from .models import Task
from django.contrib.auth.models import User
from datetime import datetime


class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Task
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'tasks']

