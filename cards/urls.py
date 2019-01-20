from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_list),
    path('new/', views.user_file_create),
]
