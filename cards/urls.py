from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_file_create),
    path('01/', views.word_list_01),
    path('02/', views.word_list_02),
    path('03/', views.word_list_03),
    path('04/', views.word_list_04),
    path('05/', views.word_list_05),
    path('new/', views.user_file_create),
    path('training/', views.user_training),
    path('training_plus/', views.user_training_plus),
    path('training_2plus/', views.user_training_2plus),
    path('training_minus/', views.user_training_minus),
]
