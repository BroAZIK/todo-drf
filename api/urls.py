from django.urls import path

from .views import TaskView, TaskDetailView, UsersView


urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('users/', UsersView.as_view()),
]
