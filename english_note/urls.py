from django.urls import path
from . import views

app_name = 'english'
urlpatterns = [
    path('', views.english_note_home_page, name='home-page'),
    path('create/', views.new_page, name='create'),
    path('<str:id>/edit/', views.edit_word, name='edit'),
    path('view_class/<str:listName>/', views.view_class, name='view-class'),
    path('word_card/<str:Class>/<str:memorize>/', views.word_card, name='word-card')
]