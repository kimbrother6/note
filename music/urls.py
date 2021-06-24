from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'music'
urlpatterns = [
    path('', views.music_home_page, name='home-page'),
    path('new/', views.new_song, name='new'),
    path('list_player/<str:list_name>/', views.list_player, name='list-player'),
    path('<int:id>/play', views.music_player, name='music-player'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('view_artist/', views.view_artist, name='view-artist'),
]
