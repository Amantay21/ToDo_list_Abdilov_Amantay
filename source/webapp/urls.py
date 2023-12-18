from django.urls import path
from webapp.views import TaskCreateView, delete_task, task_delete_view, \
    IndexView, TaskView, TaskUpdateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('task/add/', TaskCreateView.as_view(), name='tasks_create'),
    path('task/<int:pk>', TaskView.as_view(), name='tasks_view'),
    path('task/delete/', delete_task, name='delete_task'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', task_delete_view, name='task_delete')
]