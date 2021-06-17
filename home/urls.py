from os import name
from django.conf import settings # new
from django.urls import path, include # new
from . import views

urlpatterns = [
    path('math/', include('math_note.urls', namespace='math')),
    path('english/', include('english_note.urls', namespace='english')),
    path('music/', include('music.urls', namespace='music')),
    path('', views.home_page)
]