from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'math'
urlpatterns = [
    path('', views.HomePageView, name='home-page'),
    path('new/', views.newPage, name='create'),
    path('<int:id>/', views.detailPage, name='detail-page')
]