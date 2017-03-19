from django.db import models

# Create your models here

class Card(models.Model):
    username=models.CharField(default="wrecodde", 
max_length=25)

    email=models.EmailField(default="wrecodde@gmail.com")
    password=models.CharField(default="decodded", 
max_length=45)
    def __str__(self):
        return self.username
