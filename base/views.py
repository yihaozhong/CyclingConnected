from django.shortcuts import render, redirect
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
    form = RoomForm() # create a form
    if request.method == 'POST': # send the post data
        form = RoomForm(request.POST) # add the post data to the form 
        if form.is_valid(): # if it is valid
            form.save() # save it to database
            return redirect('home') # return to the home page

    context = {'form': form}
    return render(request, 'base/room_form.html', context)
# function, urls 

def updateRoom(request, pk): # pk for primary key
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room) # prefill with the room value to form

    if request.method == 'POST':
        form = RoomForm(request.POST, instance= room)
        if form.is_valid(): # if it is valid
            form.save() # save it to database
            return redirect('home') # return to the home page

    context = {'form': form}
    return render(request, 'base/room_form.html', context)