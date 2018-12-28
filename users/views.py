from django.shortcuts import render

def index(request):
    title = "Main"
    message = "Cards for easy memorization!"
    header = "Personal Data" 

    data = {"title": title, "message": message,  "header": header}
    return render(request, "index.html", context=data)
