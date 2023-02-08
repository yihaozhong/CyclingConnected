from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.db.models import Q

from django.contrib.auth.decorators import login_required

from .models import Room, Topic
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

# dont use login()
def loginPage(request):
    if request.method == "POST":
        # get the user name and pwd from user 
        username = request.POST.get('username')
        password = request.POST.get('password')

        # check exist
        try:
            user = User.objects.get(username = username)
        except:
            messages.error(request, 'User does not exist!')
        
        # check the pwd
        user = authenticate(request, username = username, password = password)
        # login in - redict to home
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR Password Not CORRECT!')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # search bar filter 
    rooms = Room.objects.filter(
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q))

    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms': rooms, 'topics': topics, 'room_count':room_count}
    return render(request, 'base/home.html', context)



def room(request, pk):
        # room read from the database
        # use get() from the datatable
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

@login_required(login_url = '/login')
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

def deleteRoom(request, pk):
    room = Room.objects.get(id = pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})