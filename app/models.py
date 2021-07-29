from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import DO_NOTHING
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# Create your models here.
User=get_user_model()

class Room(models.Model):
    name=models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender=models.ForeignKey(User,related_name='sent_messages',on_delete=models.CASCADE,null=True)
    receiver=models.ForeignKey(User,related_name='received_messages',on_delete=models.CASCADE,null=True)
    message=models.TextField()
    seen=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now_add=True)
    room=models.ForeignKey(Room,related_name='message',on_delete=models.CASCADE, null=True)


    class Meta:
        ordering=['date_created']


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_image=models.ImageField(default='default.jpeg', upload_to='Profilepics/')
    bio=models.CharField(max_length=1000,null=True, default="My Bio")
    email=models.EmailField(max_length=200,null=True)
    room=models.ForeignKey(Room,related_name='profile',on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.user} Profile'

    @receiver(post_save,sender=User)
    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save,sender=User)
    def save_user_profile(sender,instance,**kwargs):
        print("signal activated---->>>", dir(instance))
        instance.profile.save

