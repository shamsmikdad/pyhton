from django.shortcuts import render
from django.http import HttpResponse
from django.utils.timezone import datetime

# Create your views here.

def index(request):
    return render(request,"hi/index.html")

def age(recuest,birthday):
    year = datetime.today().year
    yourAge = year-birthday
    return HttpResponse(yourAge)

def gere(recuest,yourname):
    return HttpResponse (f"hello hi: {yourname}")
