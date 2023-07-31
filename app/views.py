from django.shortcuts import render
from .models import Blog


def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'home.html', {'blogs': blogs})


def blog_all(request):
    blog = Blog.objects.all()
    return render(request, 'index.html', {'blog': blog})
