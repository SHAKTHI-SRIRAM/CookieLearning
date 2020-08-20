from django.urls import path
from . import views

urlpatterns = [
    path('', views.htmlcss_home, name='htmlcss-home'),
    path('htmlcss-html/', views.htmlcss_html, name='htmlcss-html'),
    path('htmlcss-css/', views.htmlcss_css, name='htmlcss-css'),
    path('htmlcss-materialize/', views.htmlcss_materialize, name='htmlcss-materialize'),
]
