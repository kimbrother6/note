from music.models import Song
from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song
from sqlalchemy import create_engine
import youtube_dl
import pandas as pd

engine = create_engine("sqlite:////Users/cubest_june/hj-django/note/db.sqlite3")

# Create your views here.
def music_home_page(request): #메인 페이지를 호출해주는 함수
    song = Song.objects.all()

    with engine.connect() as conn, conn.begin():
            data = pd.read_sql_table("music_song", conn)
    class_list = data['Class'].unique()

    return render(request, 'music/home.html', {'song': song, 'class_list': class_list})

def new_song(request): #form
    if request.method == 'POST':
        song_title = request.POST['song_title']
        song_url = request.POST['song_url']
        Class = request.POST['Class']
        song = 'media/song/{}.mp3'.format(song_title)
        ydl_opt = {
            'format': 'bestaudio/best',
            'outtmpl': 'media/song/{}.mp3'.format(song_title)
        }

        with youtube_dl.YoutubeDL(ydl_opt) as ydl:
            ydl.download(['{}'.format(song_url)])

        new_snog = Song(
            song_title = song_title,
            song_url = song_url,
            Class = Class,
            song = song
        )
        new_snog.save()
        print(song)

        return redirect('music:music-player', id=new_snog.id)
    else:
        form = SongForm
        return render(request, 'music/forms.html', {'form': form})

def music_player(request, id): #음악을 플래이시켜주는 페이지를 호출해주는 함수
    model = Song.objects.get(id=id)
    print(model)
    return render(request, 'music/music_player.html', {'model': model})