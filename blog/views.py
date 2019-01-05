from django.shortcuts import render
from .models import Post
from django.utils import timezone

def post_list(request):
    notes = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog.html', {'notes': notes})

def post_anons(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'ru.html', {'posts': posts})
