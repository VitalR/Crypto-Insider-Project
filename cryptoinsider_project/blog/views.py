from django.shortcuts import render, redirect
from .models import Post


def blog(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html')
