from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from .models import *
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['get','post'])
def home(request):
    return render(request,'home.html')
def depot(request, pk):
    
    pass
def bag():
    pass
