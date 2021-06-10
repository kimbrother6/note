from django.urls import path
from . import views
# from .views import CreatePostView

urlpatterns = [
    path('', views.HomePageView, name='list-page'),
    path('new/', views.newPage, name='new-page'),
    path('<int:id>/', views.detailPage, name='detail-page')
]