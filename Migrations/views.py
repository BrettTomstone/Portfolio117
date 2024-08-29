from django.shortcuts import render
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects_list(request):

    projects = Project.objects.all()

    return render(request, 'content/projects_list.html', {
        'projects' : projects
    })
def new_project(request):

    form = ProjectForm()

    return render(request, 'content/new_project.html', {
        'form': form
    })
