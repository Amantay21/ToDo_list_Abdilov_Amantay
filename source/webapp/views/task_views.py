from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from webapp.forms import TaskForms
from webapp.models import Task, Project
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView


class TaskView(TemplateView):
    template_name = 'tasks/tasks_view.html'
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        context['task'] = task
        return context


class TaskCreateView(PermissionRequiredMixin, CreateView):
    template_name = 'tasks/tasks_create.html'
    form_class = TaskForms
    permission_required = 'webapp.add_task'

    def has_permission(self):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        return super().has_permission() and self.request.user in project.users.all()

    def form_valid(self, form):
        project = get_object_or_404(Project, pk=self.kwargs.get('pk'))
        task = form.save(commit=False)
        task.project = project
        task.save()
        form.save_m2m()
        return redirect('webapp:projects_detail_view', pk=project.pk)


class TaskUpdateView(PermissionRequiredMixin, UpdateView):
    template_name = 'tasks/task_update.html'
    model = Task
    form_class = TaskForms
    permission_required = 'webapp.change_task'

    def has_permission(self):
        project = self.get_object().project
        return super().has_permission() and self.request.user in project.users.all()

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.project.pk})


class TaskDeleteView(PermissionRequiredMixin, DeleteView):
    template_name = 'tasks/task_delete.html'
    model = Task
    permission_required = 'webapp.delete_task'

    def has_permission(self):
        project = self.get_object().project
        return super().has_permission() and self.request.user in project.users.all()

    def get_success_url(self):
        return reverse('webapp:projects_detail_view', kwargs={'pk': self.object.project.pk})
