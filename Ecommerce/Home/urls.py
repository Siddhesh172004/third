
from .import views
from django.urls import path
urlpatterns = [
    path('',views.Home1),
    path('login/',views.Login)
]

