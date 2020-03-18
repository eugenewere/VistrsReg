from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from visitorsfront import views

app_name='Visitors'
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.loginuser, name='login'),
    path('contuctus', views.contuctus, name='contuctus')
]