from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject

# Create your views here.


def index(request):
    title = 'django course!!!'
    return render(request, 'index.htm', {
        'title': title
    })


def about(request):
    return render(request, 'about.htm')


def hello(request, username):
    return HttpResponse("<h2>Hello %s <h2>" % username)


def projects(request):
   # projects= list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.htm', {
        'projects': projects
    })


def tasks(request):
    # task = Task.objects.get(title= title)
    tasks = Task.objects.all()
    return render(request, 'tasks/tasks.htm', {
        'tasks': tasks
    })


def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/create_task.htm', {
            'forms': CreateNewTask
        })
    else:
        Task.objects.create(
            title=request.POST['title'], description=request.POST['description'],
            project_id=2)
        return redirect('/tasks/')


def create_project(request):
    if request.method == 'GET':
        return render(request, 'projects/create_project.htm', {
            'form': CreateNewProject()
        })
    else:
        Project.objects.create(name=request.POST["name"])
        return redirect('/projects/')


def project_detail(request,id):
    project = get_object_or_404(Project, id=id)
    tasks = Task.objects.filter(project_id=id)
    return render(request, 'projects/detail.htm',{
        'project' : project,
        'tasks' : tasks
    })  