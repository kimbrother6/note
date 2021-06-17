from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'home'
urlpatterns = [
    path('', views.HomePageView, name='home-page'),
    path('new/', views.newPage, name='new-page'),
    path('<int:id>/', views.detailPage, name='detail-page')
]