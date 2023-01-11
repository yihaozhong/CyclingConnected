from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# function, urls

# how to present the view, rendering, handle data presentation

def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')