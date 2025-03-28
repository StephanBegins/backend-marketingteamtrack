from rest_framework import generics
from .models import TaskHeader, TaskDetail
from .serializers import TaskHeaderSerializer, TaskDetailSerializer

class TaskHeaderListCreateView(generics.ListCreateAPIView):
    queryset = TaskHeader.objects.all()
    serializer_class = TaskHeaderSerializer

class TaskHeaderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskHeader.objects.all()
    serializer_class = TaskHeaderSerializer

class TaskDetailListCreateView(generics.ListCreateAPIView):
    queryset = TaskDetail.objects.all()
    serializer_class = TaskDetailSerializer

class TaskDetailDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskDetail.objects.all()
    serializer_class = TaskDetailSerializer
