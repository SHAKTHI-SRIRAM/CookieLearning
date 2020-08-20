from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def htmlcss_home(request):
    return render(request, 'home/htmlcss-home.html')


def htmlcss_html(request):
    return render(request, 'home/htmlcss-html.html')


def htmlcss_css(request):
    return render(request, 'home/htmlcss-css.html')


def htmlcss_materialize(request):
    return render(request, 'home/htmlcss-materialize.html')


