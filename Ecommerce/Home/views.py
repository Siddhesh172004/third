from urllib import request
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
# Create your views here.
def Home1(request):
    return render(request,"homepage/index.html")

def Signin(request):
    return render(request,"homepage/signin.html")

def Signindo(request):
    if request.method == "POST":
        username = request.POST.get("email")
        email= username
        pass1= request.POST.get("password")
        pass2= request.POST.get("confirm_password")
        first_name = request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        
        # validationssssss
        if (User.objects.filter(username=username).exists()): 
            # messages.add_message(request, messages.INFO, 'Username already exist.')
            return redirect("/signin/")           
            

        if(not(len(pass1)>7 and not pass1.isalnum())):
            # messages.add_message(request, messages.INFO, 'Password must belonger then 8 characters and should contain a symbol.')
            return redirect("/signin/")
        
        if(not(pass1==pass2)):
            # messages.add_message(request, messages.INFO, 'Both the password must be same.')
            return redirect("/signin/")

        else:
            try:
                newUser = User.objects.create_user(username,email,pass1)
                newUser.first_name = first_name
                newUser.last_name = last_name
                newUser.save()
                # messages.add_message(request, messages.SUCCESS, 'Account succsessfully Created. Please Login to continue.')
                return redirect("/login/")
            except Exception as e:
                # messages.add_message(request, messages.ERROR, e)
                return redirect("/signin/")            
    else:
        # messages.add_message(request, messages.ERROR, 'Please SignIn.')
        return redirect("/login/")



def Login(request):
    return render(request,"homepage/login.html")

def Logindo(request):
    if request.method == "POST":
        username = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(username = username , password = password )

        if user is not None:
            login(request,user)
            # messages.add_message(request, messages.SUCCESS, 'LOGIN successfull!!')
            return redirect("/")

        else:
            # messages.add_message(request, messages.ERROR, 'Email or password is not valid. ')
            return redirect("/login/")
    else:
        # messages.add_message(request, messages.ERROR, 'Please Login.')
        return redirect("/login/")
    




def Mens(request):

    
    return render(request,"homepage/mens.html")


def Womens(request):
    return render(request,"homepage/womens.html")

def Cart(request):
    return render(request,"homepage/cart.html")



def Kids(request):
    return render(request,"homepage/kids.html")


def ContactUs(request):
    return render(request,"homepage/contact.html")




    