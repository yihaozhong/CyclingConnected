from django.shortcuts import render
from django.http import HttpResponse

from .models import Room
from .forms import RoomForm
# Create your views here.


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

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        
    context = {'form': form}
    return render(request, 'base/room_form.html', context)
# function, urls 
