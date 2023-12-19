from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TaskForms
from webapp.models import Task
from django.views.generic import View, TemplateView


class IndexView(View):

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.all()
        context = {
            'tasks': tasks
        }
        return render(request, 'index.html', context)


class TaskView(TemplateView):
    template_name = 'tasks_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task'] = get_object_or_404(Task, pk=kwargs.get('pk'))
        return context


class TaskCreateView(TemplateView):
    template_name = 'tasks_create.html'
    form_class = TaskForms

    def form_valid(self, form):
        self.task = form.save()
        return redirect('tasks_view', pk=self.task.pk)
    # def get(self, request, *args, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = TaskForms()
    #     return render(request, 'tasks_create.html', context=context)
    #
    # def post(self, request, *args, **kwargs):
    #     form = TaskForms(data=request.POST)
    #     if form.is_valid():
    #         types = form.cleaned_data.pop('types')
    #         task = Task.objects.create(
    #             title=form.cleaned_data['title'],
    #             description=form.cleaned_data['description'],
    #             status=form.cleaned_data['status'],
    #         )
    #         task.types.set(types)
    #         return redirect('tasks_view', pk=task.pk)
    #     return render(request, 'tasks_create.html', {'form': form})


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    form_class = TaskForms

    def dispatch(self, request, *args, **kwargs):
        self.task = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def get_object(self):
        return get_object_or_404(Task, pk=self.kwargs.get('pk'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.task
        return kwargs

    def form_valid(self, form):
        form.save()
        return redirect('article_view', pk=self.task.pk)


class TaskDeleteView(View):
    def get(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        return render(request, 'task_delete.html', {'task': task})

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        task.delete()
        return redirect('index')




