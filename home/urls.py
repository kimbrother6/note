from django.conf import settings # new
from django.urls import path, include # new
from . import views

urlpatterns = [
    path('math_note/', include('math_note.urls'), name='math-note'),
    path('english_note/', include('english_note.urls'), name='english-note'),
    path('', views.home_page)
]