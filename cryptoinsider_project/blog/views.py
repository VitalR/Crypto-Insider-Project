from django.shortcuts import render, redirect

posts = [
    {
        'author': 'John Snow',
        'title': 'Blog Post',
        'content': 'This is post content',
        'date_posted': 'September 12, 2020'
    },
    {
        'author': 'Test User',
        'title': 'Blog Post 2',
        'content': 'This is post content 2',
        'date_posted': 'September 12, 2020'
    }

]


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html')
