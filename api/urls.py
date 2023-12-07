from django.urls import path

from .views import TaskView,TaskDetailView


urlpatterns = [
    path('', TaskView.as_view()),
    path('<int:pk>/', TaskDetailView.as_view())
]
