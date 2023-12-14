from django.urls import path

from .views import TaskView, TaskDetailView, UsersView

from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken


urlpatterns = [
    path('tasks/', TaskView.as_view()),
    path('tasks/<int:pk>/', TaskDetailView.as_view()),
    path('users/', UsersView.as_view()),
    path('users/login/', obtain_auth_token),
    # path('users/login/', ObtainAuthToken.as_view()),
]
