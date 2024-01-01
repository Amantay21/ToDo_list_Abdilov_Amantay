from django.urls import path

from webapp.views.project_views import ProjectsView
from webapp.views.task_views import TaskCreateView, \
     TaskView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', ProjectsView.as_view(), name='index'),
    path('task/add/', TaskCreateView.as_view(), name='tasks_create'),
    path('task/<int:pk>', TaskView.as_view(), name='tasks_view'),
    path('task/<int:pk>/update', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete')
]