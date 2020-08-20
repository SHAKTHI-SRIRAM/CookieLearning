from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def git_home(request):
    return render(request, 'home/git-home.html')


def git_git(request):
    return render(request, 'home/git-git.html')


def git_github(request):
    return render(request, 'home/git-github.html')
