from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

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


def task_details(request, pk):
    task = get_object_or_404(TaskManage, pk=pk)
    return render(request, 'task_details.html', {'task': task})


def task_update(request, pk):
    task = get_object_or_404(TaskManage, pk=pk)

    if request.method == "POST":
        task.description = request.POST.get('description')
        task.status = request.POST.get("status")
        task.deadline = request.POST.get("deadline")
        task.detailed_description = request.POST.get("detailed_description")
        task.save()
        return redirect('task_details', pk=task.pk)

    return render(request, 'task_update.html', context={'task': task})


def task_delete(request, pk):
    task = get_object_or_404(TaskManage, pk=pk)
    if request.method == "GET":
        return render(request, "delete_task.html", context={'task': task})
    else:
        task.delete()
        return redirect('index')
