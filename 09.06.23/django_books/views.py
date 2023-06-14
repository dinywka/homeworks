from django.shortcuts import render, redirect
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def post_book(request):
    return HttpResponse("post")

def update_book(request):
    return HttpResponse("update")

def get_book(request):
    return HttpResponse("get")

def delete_book(request):
    return HttpResponse("delete")