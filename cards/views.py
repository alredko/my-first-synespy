from django.shortcuts import render
from .models import Word

def status_list(request):
    status = Word.objects.filter(num=1)
    return render(request, {'status': status})

def word_list(request):
    words = Word.objects.get(word='juice')
    return render(request, 'card03.html', {'words': words})
