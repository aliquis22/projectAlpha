from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import Group

def home(request):
    organisations_group = Group.objects.get(name='Organisations')
    organisations_users = organisations_group.user_set.all()

    return render(request, 'reservation/index.html', {'organisations_users': organisations_users})

def about(request):
    return render(request, 'reservation/about.html')

def reservation(request):
    return HttpResponse('<h1>Главная</h1>')

