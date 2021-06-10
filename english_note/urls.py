from django.urls import path
from . import views
# from .views import CreatePostView

urlpatterns = [
    path('', views.english_note_home_page, name='home-page'),
    path('new/', views.new_page, name='new-page'),
    # path('blind/', views.blind_detail_page, name='blind-page'),
    # path('open/<int:id>/', views.open_detail_page, name='open-page'),
    path('sentenceCard/<str:listName>/<int:listId>/', views.sentenceCard, name='sentenceCard')
]