from django.shortcuts import render


#lista
def lista_tasks(request):
    return render(request, 'tasks/list_tasks.html')
