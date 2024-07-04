from django.urls import path
from . import views
from .views import index, create_task, task_details, task_update, task_delete

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_task, name='create_task'),
    path('task/<int:pk>/', task_details, name='task_details'),
    path('task/<int:pk>/update/', task_update, name='task_update'),
    path("task/<int:pk>/delete", task_delete, name='task_delete')
]
