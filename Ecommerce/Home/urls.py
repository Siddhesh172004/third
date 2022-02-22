
from .import views
from django.urls import path
urlpatterns = [
    path('',views.Home1),
    path('mens/',views.Mens),
    path('womens/',views.Womens),
    path('cart/',views.Cart),
    path('kids/',views.Kids),
    path('contact/',views.ContactUs),
    path('mens/detail/<int:id>',views.Detail),

    

    path('signin/',views.Signin),
    path('login/',views.Login),
    path('signindo/',views.Signindo),
    path('logindo/',views.Logindo),
    
  
]

