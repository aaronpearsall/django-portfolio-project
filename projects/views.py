from django.shortcuts import render
from projects.models import Project
from django.http import HttpResponse

# Create your views here.
def all_projects(request):
    #query the db to return all project objects
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects' : projects})

def project_detail(request, pk):
    #passed on by the cowboy loop
    project = Project.objects.get(pk=pk)
    return render(request, 'projects/detail.html',{'project': project})
