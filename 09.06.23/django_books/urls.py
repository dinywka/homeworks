from django.contrib import admin
from django.urls import path
from django_books import views

urlpatterns = [
    path('', views.home),
    path('get-book/<int:book_id>/', views.get_book, name='get_book')
]