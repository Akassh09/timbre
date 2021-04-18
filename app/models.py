from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    singer = models.CharField(max_length=100)
    album = models.CharField(max_length=200,default='Untitled')
    tags = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pics')
    song = models.FileField(upload_to='audio')

    def __str__(self):
        return self.name

class Liked(models.Model):
    liked_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    video_id = models.CharField(max_length=10000,default='')

    def __str__(self):
        return self.user.username