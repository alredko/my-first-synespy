"""synespy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views
from django.views.generic import TemplateView

urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'ru/', views.post_list, name="ru.html"),
    path(r'cabinet/', TemplateView.as_view(template_name="cabinet.html")),
    path(r'card01/', TemplateView.as_view(template_name="card01.html")),
    path(r'card02/', TemplateView.as_view(template_name="card02.html")),
    path(r'card03/', TemplateView.as_view(template_name="card03.html")),
    path(r'card04/', TemplateView.as_view(template_name="card04.html")),
    path(r'card05/', TemplateView.as_view(template_name="card05.html")),
    path(r'lessons/', TemplateView.as_view(template_name="lessons.html")),
    path(r'admin/', admin.site.urls),
]
