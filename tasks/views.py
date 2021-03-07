from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from django.db.models import Q
from .models import TaskModel
from .forms import TaskForm
from django.views.generic import ListView


#lista tasks sira hotu no pajina
def lista_tasks(request):
    tasks_list = TaskModel.objects.all().order_by('id')

    #Kria pajina
    #page = request.GET.get('page', 1)
    paginator = Paginator(tasks_list, 3)
    if request.GET.get('page'):
        # Grab the current page from query parameter
        page = int(request.GET.get('page', 1))
    else:
        page = None
    try:
        tasks = paginator.page(page)
    except PageNotAnInteger:
        tasks = paginator.page(1)
    except EmptyPage:
        tasks = paginator.page(paginator.num_pages)

    tasks_count = TaskModel.objects.all().count() #konta total task ne'ebe kria ona no hatudu iha template
    # tasks_count = TaskModel.objects.filter(titlu__contains='Ba').count() #konta kada titlu ne'ebe konteudu liafuan ba
    users = User.objects.all() #query user fo sai iha template

    context = {
            'tasks': tasks,
            'tasks_count': tasks_count,
            'users': users,
        }
    return render(request, 'tasks/list_tasks.html', context)


#Hare detallu task
def detallu_tasks(request, pk):
    task = get_object_or_404(TaskModel, pk=pk) 
    context ={
            'task': task
        }
    return render(request, 'tasks/detallu_tasks.html', context)


# kria task
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


#search fbv
def search_tasks(request):
    query = request.GET.get('q')
    queryset = (Q(titlu__icontains=query) | Q(deskrisaun__icontains=query) | Q(user__username=query))
    tasks = TaskModel.objects.filter(queryset).distinct()
    context = {
           'tasks': tasks, 'query': query
        }
    return render(request, 'tasks/buka_tasks.html', context)



'''
#Karik ita search uza CBV
class SearchTaskView(ListView):
    model = TaskModel
    template_name = 'tasks/search_tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = TaskModel.objects.filter(
                Q(titlu__icontains=query) | Q(deskrisaun__icontains=query) | Q(user__username=query)
                )
        return object_list
'''
