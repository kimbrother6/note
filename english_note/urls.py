from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'english'
urlpatterns = [
    path('', views.english_note_home_page, name='home-page'),
    path('new/', views.new_page, name='new'),
    path('word_card/<str:listName>/', views.word_card, name='word-card')
]