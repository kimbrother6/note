from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'math'
urlpatterns = [
    path('', views.HomePageView, name='home-page'),
    path('create/', views.newPage, name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit/', views.edit, name='edit'),
    path('<int:id>/delete/', views.delete, name='delete'),
]