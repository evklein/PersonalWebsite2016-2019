from django.conf.urls import url
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import BlogPost

def blog(request):
    all_posts  = BlogPost.objects.all().order_by('-date_posted')
    context = { 'all_posts': all_posts }
    template = loader.get_template('blog/blog_listing.html')
    return HttpResponse(template.render(context, request))

def steganography(request):
    post = BlogPost.objects.get(title="Imaging Steganography with Stegory")
    context = { 'post' : post }
    template = loader.get_template('blog/blog_post.html')
    return HttpResponse(template.render(context, request))

def recording(request):
    post = BlogPost.objects.get(title="Start and Stop Recording with PCM Data and Android")
    context = { 'post' : post }
    template = loader.get_template('blog/blog_post.html')
    return HttpResponse(template.render(context, request))
