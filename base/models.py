from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# handles data logic, interacts with database

# where we create database tables
# we create python class, representing the database
    # each variable is each columns 
    # essentially a model of tables, so why it is called models

# create a topic
class Topic(models.Model):
    name = models.CharField(max_length = 200)


    def __str__(self):
        return self.name


# create a room class, inherient from Django models
class Room(models.Model):
    host = models.ForeignKey(User, on_delete =  models.SET_NULL, null = True)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    name = models.CharField(max_length= 200)
    description = models.TextField(null = True, blank= True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']
    def __str__(self):
        return self.name


# create a message
class Message(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    room = models.ForeignKey(Room, on_delete = models.CASCADE)
        # when the parent is deleted, set null or cascade (deleted)\
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50] # return first 50 msg



