from music.models import Song
from django.shortcuts import render, redirect
from .forms import SongForm
from .models import Song
import youtube_dl


# Create your views here.
def music_home_page(request):
    # ydl_opt = {
    #     'outtmpl': 'song/%(title)s.%(ext)s'
    # }
    # with youtube_dl.YoutubeDL(ydl_opt) as ydl:
    #     ydl.download(['https://www.youtube.com/watch?v=DbXMjAYSa68'])
    return render(request, 'music/home.html')

def new_song(request):
    if request.method == 'POST':
        newPost = Song(
            song_title = request.POST['song_title'],
            song = request.FILES['song'],
            Class = request.POST['Class'],
        )
        newPost.save()
        return redirect('home-page')
    else:
        form = SongForm
        return render(request, 'music/forms.html', {'form': form})

def music_player(request):
    model = Song.objects.get(id=1)

    return render(request, 'music/music_player.html', {'model': model})