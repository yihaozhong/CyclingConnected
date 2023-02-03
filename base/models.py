from django.db import models

# Create your models here.

# handles data logic, interacts with database

# where we create database tables
# we create python class, representing the database
    # each variable is each columns 
    # essentially a model of tables, so why it is called models

# create a room class, inherient from Django models
class Room(models.Model):
    # host =
    # topic = 
    name = models.CharField(max_length= 200)
    description = models.TextField(null = True, blank= True)
    # participants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name