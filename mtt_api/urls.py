from django.urls import path
from .views import TaskHeaderListCreateView, TaskHeaderDetailView, TaskDetailListCreateView, TaskDetailDetailView

urlpatterns = [
    path('task-headers/', TaskHeaderListCreateView.as_view(), name='task-header-list-create'),
    path('task-headers/<int:pk>/', TaskHeaderDetailView.as_view(), name='task-header-detail'),
    path('task-details/', TaskDetailListCreateView.as_view(), name='task-detail-list-create'),
    path('task-details/<int:pk>/', TaskDetailDetailView.as_view(), name='task-detail-detail'),
]
