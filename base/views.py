from django.shortcuts import render
from django.http import HttpResponse

from .models import Room
# Create your views here.

# function, urls

# how to present the view, rendering, handle data presentation


# rooms = [
#     {'id': 1, 'name': 'lets cycling'},
#     {'id': 2, 'name': 'Gear Shoper'},
#     {'id': 3, 'name': 'Pro rider'},
# ]

# tag: {% %}
# template: {{ }}

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)


def room(request, pk):
        # room read from the database
        # use get() from the datatable
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)
