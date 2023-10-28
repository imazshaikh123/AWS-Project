from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("",views.homepage, name='home'),
    path("register",views.register, name='register'),
    path("questions",views.questions, name='questions'),
]
