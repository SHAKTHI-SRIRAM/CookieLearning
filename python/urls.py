from django.urls import path
from . import views
from home import views as home_views

urlpatterns = [
    path('', views.python_home, name='python-home'),
    path('python-beginner/', views.python_beginner, name='python-beginner'),
    path('python-gui/', views.python_gui, name='python-gui'),
    path('python-datascience/', views.python_datascience, name='python-datascience'),
    path('python-django/', views.python_django, name='python-django'),
]
