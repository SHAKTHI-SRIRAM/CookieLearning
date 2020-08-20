from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def databases_home(request):
    return render(request, 'home/databases-home.html')


def databases_mysql(request):
    return render(request, 'home/databases-mysql.html')


def databases_postgresql(request):
    return render(request, 'home/databases-postgresql.html')
