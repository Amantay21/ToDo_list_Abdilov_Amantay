from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect


def index_view(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'index.html', context)


def task_view(request, *args, pk, **kwargs):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'tasks_view.html', {'task': task})


def delete_task(request):
    if request.method == "POST":
        task_id = request.POST.get('id')
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return redirect('index')



def create_task_view(request):
    if request.method == "GET":
        return render(request, 'tasks_create.html', {'status_choices': status_choices})
    elif request.method == "POST":
        task = Task.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            date_of_completion=request.POST.get('date_of_completion')
        )

        return redirect('tasks_view', pk=task.pk)

def update_task_view(request,pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "GET":
        return render(request, 'task_update.html', {'task': task, 'status_choices': status_choices})
    elif request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.status = request.POST.get('status')
        task.date_of_completion = request.POST.get('date_of_completion')
        task.save()
        return redirect('tasks_view', pk=task.pk)
def task_delete_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        return render(request, 'task_delete.html', context={'task': task})
    elif request.method == 'POST':
        task.delete()
        return redirect('index')