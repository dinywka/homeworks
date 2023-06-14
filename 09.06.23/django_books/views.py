from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django_books import models



def home(request):
    select_orm = models.Books_tab.objects.all()
    for i in select_orm:
        print(type(i), i)
        print(i.book_name, i.author, i.category, i.username)
    # print(select_orm)
    # print(type(select_orm))

    return render(request, 'home.html', context={"select_orm": select_orm})

def post_book(request):
    return HttpResponse("post")

def update_book(request):
    return HttpResponse("update")

def get_book(request, book_id):
    return HttpResponse("get")

def delete_book(request):
    return HttpResponse("delete")