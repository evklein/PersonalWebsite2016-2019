from django.conf.urls import url
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Project

def portfolio(request):
    return render_to_response('portfolio_listing.html')

def infinity_table(request):
    page_data = Project.objects.get(title="Infinity Table with TabLED")
    context = { 'page_data' : page_data }
    template= loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def pluto(request):
    page_data = Project.objects.get(title="Pluto")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def dj_say(request):
    page_data = Project.objects.get(title="dj-say")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def kill_switch(request):
    page_data = Project.objects.get(title="Kill-Switch for Chrome")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def song_friend(request):
    page_data = Project.objects.get(title="Song-Friend")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def stegory(request):
    page_data = Project.objects.get(title="Stegory")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def hex_helper(request):
    page_data = Project.objects.get(title="Hex-Helper")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def aes0p(request):
    page_data = Project.objects.get(title="aes0p")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))

def ghostly(request):
    page_data = Project.objects.get(title="Ghostly")
    context = { 'page_data': page_data }
    template = loader.get_template('projects/project.html')
    return HttpResponse(template.render(context, request))
