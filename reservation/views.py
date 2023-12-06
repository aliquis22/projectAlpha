from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'reservation/index.html')

def about(request):
    return render(request, 'reservation/about.html')

def reservation(request):
    return HttpResponse('<h1>Главная</h1>')