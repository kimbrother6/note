from django.db import models

# Create your models here.

class Song(models.Model):
    artist = models.CharField(max_length=30, null=True, blank=True)
    song_title = models.CharField(max_length=30, null=True)
    song_url = models.CharField(max_length=1000, null=True)
    Class = models.CharField(max_length=30, null=True, blank=True)
    song = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.song_title
