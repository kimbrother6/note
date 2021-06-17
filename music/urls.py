from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'music'
urlpatterns = [
    path('', views.music_home_page, name='home-page'),
    path('new/', views.new_song, name='new'),
    path('music_player/<int:id>/', views.music_player, name='music-player'),
]
