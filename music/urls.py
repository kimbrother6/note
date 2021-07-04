from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'music'
urlpatterns = [
    path('', views.music_home_page, name='home-page'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('list_player/<str:list_name>/', views.list_player, name='list-player'),
    path('view_artist/', views.view_artist, name='view-artist'),
]