from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    pic = models.ImageField(upload_to="pic")
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self) -> str:
        return f'User:{self.user.username}'


class Rooms(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="pic")
    
    def __str__(self) -> str:
        return f'room:{self.title}'


    

class Message(models.Model):
    text = models.TextField()
    time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    room = models.ForeignKey(Rooms,on_delete=models.CASCADE)
    time = models.TimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f'User:{self.user.username} text:{self.text} room:{self.room}'







