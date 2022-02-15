
from .import views
from django.urls import path
urlpatterns = [
    path('',views.Home1),
    path('login/',views.Login),
    path('mens/',views.Mens),
    path('womens/',views.Womens),
    path('cart/',views.Cart),
    path('signin/',views.Signin),
    path('kids/',views.Kids),
    path('contact/',views.ContactUs)
    
  
]

