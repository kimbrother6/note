from django.urls import path
from . import views

app_name = 'english'
urlpatterns = [
    path('', views.english_home_page, name='home-page'),
    path('create/', views.create, name='create'),
    path('<int:id>/edit/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    path('<str:Class>/write/', views.write, name='write'),
    path('word_card/<str:Class>/<str:memorize>/', views.word_card, name='word-card'),
    path('view_class/<str:listName>/', views.view_class, name='view-class'),
]