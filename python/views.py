from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def python_home(request):
    return render(request, 'home/python-home.html')


def python_beginner(request):
    return render(request, 'home/python-beginner.html')


def python_gui(request):
    return render(request, 'home/python-gui.html')


def python_datascience(request):
    return render(request, 'home/python-datascience.html')

def python_django(request):
    return render(request, 'home/python-django.html')
