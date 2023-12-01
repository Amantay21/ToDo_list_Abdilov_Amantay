from django.urls import path
from webapp.views import index_view, create_task_view, task_view, delete_task

urlpatterns = [
    path('', index_view, name='index'),
    path('tasks/add/', create_task_view, name='tasks_create'),
    path('task/<int:pk>', task_view, name='tasks_view'),
    path('delete/', delete_task, name='delete_task')
]