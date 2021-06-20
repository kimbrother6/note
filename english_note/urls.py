from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'english'
urlpatterns = [
    path('', views.english_note_home_page, name='home-page'),
    path('create/', views.new_page, name='create'),
    path('<str:id>/edit/', views.edit_word, name='edit'),
    path('word_card/<str:listName>/', views.word_card, name='word-card')

]