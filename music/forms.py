from django import forms
from django.db.models import fields
from .models import Song

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['artist', 'song_title', 'song_url', 'Class']