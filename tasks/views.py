from django.shortcuts import render
from .models import TaskModel


#lista
def lista_tasks(request):
    tasks = TaskModel.objects.all() 

    context = {
            'tasks': tasks
        }
    return render(request, 'tasks/list_tasks.html', context)
