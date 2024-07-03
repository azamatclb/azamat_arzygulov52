from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from webapp.models import TaskManage


# Create your views here.

def index(request):
    tasks = TaskManage.objects.order_by("deadline")
    return render(request, 'index.html', context={"tasks": tasks})


def create_task(request):
    if request.method == 'POST':
        description = request.POST.get('description')
        detailed_description = request.POST.get('detailed_description')
        status = request.POST.get('status')
        deadline = request.POST.get('deadline')

        task = TaskManage.objects.create(
            description=description,
            detailed_description=detailed_description,
            status=status,
            deadline=deadline
        )
        return redirect('index')
    else:
        task = TaskManage()
    return render(request, 'create_task.html', context={'task': task})


def task_details(request, *args, pk, **kwargs):
    try:
        task = TaskManage.objects.get(id=pk)
        pass
    except TaskManage.DoesNotExist:
        return HttpResponseRedirect('/')
    return render(request, 'task_details.html', context={'task': task})
