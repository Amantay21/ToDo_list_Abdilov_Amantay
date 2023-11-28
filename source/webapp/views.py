from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webapp.models import Task, status_choices
from django.http import HttpResponseRedirect


def index_view(request):
    tasks = Task.objects.all()
    context = {"tasks": tasks}
    return render(request, 'index.html', context)


def task_view(request):
    task_id = request.GET.get('id')
    tasks = Task.objects.get(id=task_id)
    context = {"tasks": tasks, 'status_choices': status_choices}
    return render(request, 'tasks_view.html', context)


def delete_task(request):
    task_id = request.GET.get('id')
    task = get_object_or_404(Task, id=task_id)

    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect(reverse('/'))

    return HttpResponseRedirect('/')
def create_task_view(request):

    if request.method == "GET":
        return render(request, 'tasks_create.html', {'status_choices': status_choices})
    elif request.method == "POST":
        Task.objects.create(
            description=request.POST.get('description'),
            status=request.POST.get('status'),
            date_of_completion=request.POST.get('date_of_completion')
        )
        return HttpResponseRedirect('/')
