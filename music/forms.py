from django import forms

class SongForm(forms.Form):
    artist = forms.CharField(label='아티스트')
    song_title = forms.CharField(label='노래 제목')
    song_url = forms.CharField(label='노래 링크')
    Class = forms.CharField(label='분류')