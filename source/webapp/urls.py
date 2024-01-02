from django.urls import path

from webapp.views.project_views import ProjectsView, ProjectDetailView, ProjectCreateView, ProjectUpdateView, \
    ProjectDeleteView
from webapp.views.task_views import TaskCreateView, \
     TaskView, TaskUpdateView, TaskDeleteView

urlpatterns = [
    path('', ProjectsView.as_view(), name='index'),
    path('project/<int:pk>', ProjectDetailView.as_view(), name='projects_detail_view'),
    path('project/create/', ProjectCreateView.as_view(), name='projects_create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='projects_update'),
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='projects_delete'),
    path('task/<int:pk>/add/', TaskCreateView.as_view(), name='tasks_create'),
    path('task/<int:pk>', TaskView.as_view(), name='tasks_view'),
    path('task/<int:pk>/edit', TaskUpdateView.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete')
]