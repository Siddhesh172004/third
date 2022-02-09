from urllib import request
from django.shortcuts import render

# Create your views here.
def Home1(request):
    return render(request,"homepage/index.html")


def Login(request):
    return render(request,"homepage/login.html")


    