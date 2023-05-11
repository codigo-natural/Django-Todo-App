from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Task

# Create your views here.

def task_list(request):
    tasks = Task.objects.order_by('due_date', 'priority')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def task_new(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        due_date = request.POST.get('due_date')
        priority = request.POST.get('priority')

        task = Task(
            title=title,
            description=description,
            due_date=due_date,
            priority=priority,
        )
        task.save()
        return HttpResponseRedirect('/tasks/')
    
    return render(request, 'tasks/task_new.html')

def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        due_date = request.POST['due_date']
        priority = request.POST['priority']
        # completed = request.POST['completed']

        task.title = title
        task.description = description
        task.due_date = due_date
        task.priority = priority
        # task.completed = completed
        task.save()

        return HttpResponseRedirect('/tasks/')
    
    context = {
        'task': task
    }
    return render(request, 'tasks/task_edit.html', context)

def task_completed(request):
    task = Task.objects.filter(completed=True).order_by('due_date', 'priority')
    context = {
        'task': task
    }
    return render(request, 'tasks/task_completed.html', context)


def task_delete(request, pk):

    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return HttpResponseRedirect('/tasks/')
    
    context = {
        'task': task
    }
    
    return render(request, 'tasks/task_delete.html', context)