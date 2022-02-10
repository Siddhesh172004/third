from urllib import request
from django.shortcuts import render

# Create your views here.
def Home1(request):
    return render(request,"homepage/index.html")


def Login(request):
    return render(request,"homepage/login.html")

def Mens(request):
    return render(request,"homepage/mens.html")


def Womens(request):
    return render(request,"homepage/womens.html")

def Cart(request):
    return render(request,"homepage/cart.html")

def Signin(request):
    return render(request,"homepage/signin.html")



def Kids(request):
    return render(request,"homepage/kids.html")


def ContactUs(request):
    return render(request,"homepage/contact.html")




    