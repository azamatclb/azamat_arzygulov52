from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.dateparse import parse_date

from webapp.forms import TaskForm
from webapp.models import TaskManage


# Create your views here.

def index(request):
    tasks = TaskManage.objects.order_by("deadline")
    return render(request, 'index.html', context={"tasks": tasks})


def create_task(request):
    if request.method == 'POST':
        task = TaskForm(request.POST)
        if task.is_valid():
            task.save()
            return HttpResponseRedirect("/")
    else:
        task = TaskForm()
    return render(request, 'create_task.html', context={'task': task})


def task_details(request, *args, pk, **kwargs):
    try:
        task = TaskManage.objects.get(id=pk)
        pass
    except TaskManage.DoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, 'task_details.html', context={'task': task})
