from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name


class Message(models.Model):
    message=models.CharField(max_length=200000)
    date = models.DateTimeField(auto_now_add=True)
    user=models.CharField(max_length=200)
    room=models.CharField(max_length=300)
     
    def __str__(self):
        return self.message
