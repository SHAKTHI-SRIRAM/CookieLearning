from django.urls import path
from . import views

urlpatterns = [
    path('', views.databases_home, name='databases-home'),
    path('databases-mysql/', views.databases_mysql, name='databases-mysql'),
    path('databases-postgresql/', views.databases_postgresql, name='databases-postgresql'),
]
