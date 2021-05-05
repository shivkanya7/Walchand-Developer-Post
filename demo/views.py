from django.shortcuts import render
from django.http import  HttpResponse
from django.shortcuts import render,redirect
from .models import *

def display_projects(request):
    projects = Project.objects.all()
    project_list = []
    for project in projects:
        tmp_dict ={}
        tmp_dict['id'] = project.id
        tmp_dict['name'] = project.name
        tmp_dict['tagline'] = project.tag_line
        tmp_dict['photo'] = project.photo
        project_list.append(tmp_dict)

    params = {'projects' : project_list}
    for p in params['projects']:
        print(p)
    return render(request,"DisplayProjects.html",params)

def homepage(request):
    return render(request,'Homepage.html')

def login(request):
    return render(request,'Login.html')

def single_project(request,id,slug):
    print(id)
    project = Project.objects.get(id = id)

    project_info = {}
    project_info['name'] = project.name.capitalize()
    project_info['tag_line'] = project.tag_line
    project_info['photo'] = project.photo
    project_info['year'] = project.year
    project_info['domain'] = project.domain
    project_info['guide'] =project.guide
    project_info['inspiration'] = project.inspiration
    project_info['what_it_does'] = project.what_it_does
    project_info['how_we_build'] = project.how_we_build
    project_info['challenges'] = project.challenges
    project_info['accomplishment'] = project.accomplishment
    project_info['we_learned'] = project.we_learned
    project_info['whats_next'] = project.whats_next
    print(project_info)
    params = {'project' : project_info}
    return render(request,'Project.html',params)