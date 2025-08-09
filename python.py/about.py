from django.shortcuts import render
from django.urls import path
from .import views

def about(request):
    return render(request, "about.html")

urlpatterns = [
    path('', views.home, name='home')
    path('about/', views.about, name ='about')
]