from django.contrib import admin
from django.urls import path
from django_books import views

urlpatterns = [
    path('', views.home),
]