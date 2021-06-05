"""mysite hello URL Configuration"""

from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.page_home, name='index'),
]
