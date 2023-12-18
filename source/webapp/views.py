from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.forms import TaskForms
from webapp.models import Task
from django.http import HttpResponseRedirect
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

    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = TaskForms()
        return render(request, 'tasks_create.html', context=context)

    def post(self, request, *args, **kwargs):
        form = TaskForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('type')
            task = Task.objects.create(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
            )
            task.types.set(types)
            return redirect('tasks_view', pk=task.pk)
        return render(request, 'tasks_create.html', {'form': form})


class TaskUpdateView(TemplateView):
    template_name = 'task_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForms(initial={
            'title': task.title,
            'description': task.description,
            'status': task.status,
            'types': task.types.all()
        })
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        task = get_object_or_404(Task, pk=kwargs.get('pk'))
        form = TaskForms(data=request.POST)
        if form.is_valid():
            types = form.cleaned_data.pop('types')
            task.title = form.cleaned_data.get('title')
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.types.set(types)
            task.save()
            return redirect('tasks_view', pk=task.pk)
        else:
            return render(request, 'task_update.html', {'form': form})


def delete_task(request):
    if request.method == "POST":
        task_id = request.POST.get('id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('index')


# def update_task(request, pk):
#     task = get_object_or_404(Task, pk=pk)
#     if request.method == "GET":
#         form = TaskForms(initial={
#             'title': task.title,
#             'description': task.description,
#             'status': task.status,
#             'type': task.type,
#         })
#         return render(request, 'product_update.html', {'form': form, 'task': task})
#     elif request.method == "POST":
#         form = TaskForms(data=request.POST)
#         if form.is_valid():
#             task.title = request.POST.get('title')
#             task.description = request.POST.get('description')
#             task.status = request.POST.get('status')
#             task.type = request.POST.get('type')
#             task.save()
#             return redirect('index')
#         else:
#             return render(request, 'task_update.html', {'form': form})


def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')
