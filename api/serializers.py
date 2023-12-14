from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from datetime import datetime
from django.utils.timezone import now
from base64 import b64decode
from datetime import datetime

def multiple_of_ten1(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

def multiple_of_ten2(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

def multiple_of_ten3(value):
    if value % 10 != 0:
        raise serializers.ValidationError('Not a multiple of ten')

class TaskSerializer(serializers.ModelSerializer):
    score = serializers.IntegerField(validators=[multiple_of_ten1, multiple_of_ten2, multiple_of_ten3])

    class Meta:
        model = Task
        fields = '__all__'

    def validate_title(self, value):
        """
        Check that the blog post is about Django.
        """
        if value.lower() not in ['title', 'sarlavha']:
            raise serializers.ValidationError("Siz notogri title tanlagansiz.")
        return value

    def validate(self, data):
        """
        Check that start is before finish.
        """
        created_date = datetime.fromisoformat(data['created'])
        if created_date > now():
            raise serializers.ValidationError("siz notogri sanani tanlasingiz.")
        return data
        

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
