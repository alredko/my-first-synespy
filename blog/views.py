from django.shortcuts import render
from .models import Post
from django.utils import timezone

def index(request):
    title = "Main"
    message = "Cards for easy memorization!"
    header = "Personal Data" 

    data = {"title": title, "message": message,  "header": header}
    return render(request, "index.html", context=data)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'ru.html', {'posts': posts})
