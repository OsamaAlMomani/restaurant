from django.contrib import admin
from django.urls import path,include
from restaurant.views import home

urlpatterns = [
    path('',home),
]
