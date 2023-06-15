from django.contrib import admin
from django.urls import path
from django_students import views

urlpatterns = [
    path('', views.home),
]