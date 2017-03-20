from django.db import models

# Create your models here

class Card(models.Model):
    title=models.CharField(max_length=45, 
default="Card Title")
    address=models.CharField(max_length=75, 
default="URL or Platform")
    username=models.CharField(max_length=35, 
default="UserName")
    email=models.EmailField()
    password=models.CharField(max_length=125, 
default="password")
    notes=models.TextField(max_length=225, 
default="put extra notes down here")
    #type=(available list of card types)

