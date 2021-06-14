from django import forms

class SongForm(forms.Form):
    song_title = forms.CharField(widget=forms.Textarea, label='노래 제목')
    song = forms.FileField(label='노래')
    Class = forms.CharField(label='분류')