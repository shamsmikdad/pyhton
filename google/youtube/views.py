from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello World")

def ali(request):
    return HttpResponse("<h1> Hllo ali</h1> <input type='text'  placeholder='insert your weight'>")


def homam(request):
    return HttpResponse("Hello homam")

def greet(request,name):
    yourname=name
    return HttpResponse(f"Hello {yourname.capitalize()}")