from django.urls import path
from . import views

urlpatterns = [
    path('', views.javascript_home, name='javascript-home'),
    path('javascript-beginner/', views.javascript_beginner, name='javascript-beginner'),
    path('javascript-node/', views.javascript_node, name='javascript-node'),
    path('javascript-react/', views.javascript_react, name='javascript-react'),
]
