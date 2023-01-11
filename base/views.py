from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# function, urls

# how to present the view, rendering, handle data presentation


rooms = [
    {'id': 1, 'name': 'lets cycling'},
    {'id': 2, 'name': 'Gear Shoper'},
    {'id': 3, 'name': 'Pro rider'},
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})


def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'base/room.html', context)
