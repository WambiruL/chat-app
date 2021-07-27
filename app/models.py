from django.db import models

# Create your models here.
class Room(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name
post_date = models.DateTimeField(auto_now_add=True)
class Message(models.Model):
    message=models.CharField(max_length=200000)
    date = models.DateTimeField(auto_now_add=True)
    username=models.CharField(max_length=200)
    room=models.ForeignKey(Room,related_name='message')
