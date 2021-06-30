from django.urls import path
from . import views

app_name = 'english'
urlpatterns = [
    path('', views.english_note_home_page, name='home-page'),
    path('create/', views.new_page, name='create'),
    path('<int:id>/edit/', views.edit_word, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('word_card/<str:Class>/<str:memorize>/', views.word_card, name='word-card'),
    path('view_class/<str:listName>/', views.view_class, name='view-class'),
]