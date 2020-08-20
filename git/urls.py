from django.urls import path
from . import views

urlpatterns = [
    path('', views.git_home, name='git-home'),
    path('git-git/', views.git_git, name='git-git'),
    path('git-github/', views.git_github, name='git-github'),
]
