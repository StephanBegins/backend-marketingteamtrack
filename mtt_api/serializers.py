from rest_framework import serializers
from .models import TaskHeader, TaskDetail

class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskDetail
        fields = '__all__'

class TaskHeaderSerializer(serializers.ModelSerializer):
    details = TaskDetailSerializer(many=True, read_only=True)

    class Meta:
        model = TaskHeader
        fields = '__all__'
