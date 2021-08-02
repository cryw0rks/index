from django.shortcuts import render, get_object_or_404
from .models import Service, Banner, Project

def HomePage(request):
    service_list = Service.objects.filter(status=1).order_by('-create_at')
    project_list = Project.objects.filter(status=1).order_by('-create_at')[:4]
    banner_list = Banner.objects.filter(status=1).order_by('-create_at')
    
    theme_dark = request.COOKIES.get('theme', '')
    if theme_dark == 'dark':
        theme_dark = True
    else:
        theme_dark = False

    return render(request, 'home.html', { 'theme_dark': theme_dark, 'service': service_list, 'project': project_list, 'banner': banner_list })

def ServicePage(request):
    service_list = Service.objects.filter(status=1).order_by('-create_at')
    
    theme_dark = request.COOKIES.get('theme', '')
    if theme_dark == 'dark':
        theme_dark = True
    else:
        theme_dark = False

    return render(request, 'service.html', { 'theme_dark': theme_dark, 'service': service_list })

def ServiceDetail(request, slug):
    service_list = Service.objects.filter(status=1, slug=slug).order_by('-create_at')
    
    theme_dark = request.COOKIES.get('theme', '')
    if theme_dark == 'dark':
        theme_dark = True
    else:
        theme_dark = False

    return render(request, 'service_detail.html', { 'theme_dark': theme_dark, 'service': service_list[0] })

def ProjectPage(request):
    banner_list = Banner.objects.filter(status=1).order_by('-create_at')
    project_list = Project.objects.filter(status=1).order_by('-create_at')
    
    theme_dark = request.COOKIES.get('theme', '')
    if theme_dark == 'dark':
        theme_dark = True
    else:
        theme_dark = False

    return render(request, 'project.html', { 'theme_dark': theme_dark, 'project': project_list, 'banner': banner_list })

def ProjectDetail(request, slug):
    project_list = Project.objects.filter(status=1, slug=slug).order_by('-create_at')
    
    theme_dark = request.COOKIES.get('theme', '')
    if theme_dark == 'dark':
        theme_dark = True
    else:
        theme_dark = False

    return render(request, 'project_detail.html', { 'theme_dark': theme_dark, 'project': project_list[0] })

def ContactPage(request):
    theme_dark = request.COOKIES.get('theme', '')
    if theme_dark == 'dark':
        theme_dark = True
    else:
        theme_dark = False

    return render(request, 'contact.html', { 'theme_dark': theme_dark })
