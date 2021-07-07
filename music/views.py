from sqlalchemy.log import instance_logger
from music.models import Song
from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song
from sqlalchemy import create_engine
import youtube_dl
import pandas as pd
import random


engine = create_engine("sqlite:////Users/cubest_june/hj-django/note/db.sqlite3")
# with engine.connect() as conn, conn.begin():
    #data = pd.read_sql_table("music_song", conn)


def music_home_page(request): #메인 페이지를 호출해주는 함수
    song = Song.objects.all()

    with engine.connect() as conn, conn.begin():
            data = pd.read_sql_table("music_song", conn)
    class_list = data['Class'].unique()

    return render(request, 'music/home.html', {'song': song, 'class_list': class_list})

def create(request): #form
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
            artist = request.POST['artist'],
            song_title = song_title,
            song_url = song_url,
            Class = Class,
            song = song
        )
        new_snog.save()
        print(song)

        return redirect('music:detail', id=new_snog.id)
    else:
        form = SongForm
        return render(request, 'music/forms.html', {'form': form})

def detail(request, id): #음악을 플래이시켜주는 페이지를 호출해주는 함수
    song = Song.objects.get(id=id)
    return render(request, 'music/detail.html', {'song': song})

def update(request, id):
    song = Song.objects.get(id=id)
    if request.method == 'POST':
        song_form = SongForm(request.POST, instance=song)
        song_form.save()

        return redirect('music:home-page')
    else:
        form = SongForm(instance=song)
        return render(request, 'music/forms.html', {'form': form})

def list_player(request, list_name):
    songs = Song.objects.filter(Class=list_name)
    return render(request, 'music/list_player.html', {'songs': songs})



def view_artist(request):
    song = Song.objects.all()
    with engine.connect() as conn, conn.begin():
            data = pd.read_sql_table("music_song", conn)
    artist = data['artist'].unique()
    return render(request, 'music/artist.html', {'song': song, 'artist': artist})

def delete(request ,id):
    song = Song.objects.get(id=id)
    if request.method == 'POST':
        song.delete()
        return redirect('music:home-page')
    else:
        return render(request, 'home/post_confirm_delete.html', {'song': song})

def song_push(request):
    song = Song.objects.all()
    song_push = song[random.randint(0, len(song) - 1)]
    return render(request, 'music/detail.html', {'song': song_push})