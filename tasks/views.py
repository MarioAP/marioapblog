from django.shortcuts import render, get_object_or_404, redirect
from .models import TaskModel
from .forms import TaskForm


#lista tasks sira hotu
def lista_tasks(request):
    tasks = TaskModel.objects.all() 

    context = {
            'tasks': tasks
        }
    return render(request, 'tasks/list_tasks.html', context)


#Hare detallu task
def detallu_tasks(request, pk):
    task = get_object_or_404(TaskModel, pk=pk) 
    context ={
            'task': task
        }
    return render(request, 'tasks/detallu_tasks.html', context)


#kria task
def kria_tasks(request):
    form = TaskForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
            'form': form
        }    
    return render(request, 'tasks/kria_tasks.html', context)


#halo koresaun ba/hadia
def hadia_tasks(request, pk):
    task = TaskModel.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=task)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {
            'form': form
        }
    return render(request, 'tasks/hadia_tasks.html', context)

#hamoos task
def hamoos_tasks(request, pk):
    task = TaskModel.objects.get(pk=pk)
    if request.method == 'POST':
        task.delete()
        return redirect('/')

    context = {
            'task': task
        }
    return render(request, 'tasks/hamoos_tasks.html', context)
