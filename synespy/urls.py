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
from django.urls import include, path
from django.views.generic import TemplateView
from blog import views

urlpatterns = [
    path('', TemplateView.as_view(template_name="index.html")),
    path('ru/', views.post_anons, name='ru'),
    path('blog/', include('blog.urls')),
    path('card01/', include('cards.urls')),
    path('card02/', TemplateView.as_view(template_name="card02.html")),
    path('card03/', TemplateView.as_view(template_name="card03.html")),
    path('card04/', TemplateView.as_view(template_name="card04.html")),
    path('card05/', TemplateView.as_view(template_name="card05.html")),
    path('lessons/', TemplateView.as_view(template_name="lessons.html")),
    path('cabinet/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
