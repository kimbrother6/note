from django.db import models

# Create your models here.

class Song(models.Model):
    song_title = models.CharField(max_length=30, null=True, blank=True)
    song = models.FileField(upload_to='song/')
    Class = models.CharField(max_length=30, null=True, blank=True)