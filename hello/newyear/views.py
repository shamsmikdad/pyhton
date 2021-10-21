from django.shortcuts import render
from django.http import HttpResponse, request
import datetime

# Create your views here.

def index(request):
    return render(request,"hi/index.html")

def age(recuest,birthday):
    # year = datetime.today().year
    # yourAge = year-birthday
    Now = datetime.datetime.now()

    return render (request,"hi/index.html",{
        now.
    })

# def gere(request,yourname):
#     return render (request,"greet/index.html",{
#          "name": yourname.capitalize()
#     })

def mario(request):
    return render(request,"mario/index.html")
