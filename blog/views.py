from django.shortcuts import render
from .models import BlogPost

def blog_home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog_home.html', {'posts': posts})

def blog_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    return render(request, 'blog_post.html', {'post': post})
