from django.urls import path
from . import views
# from .views import CreatePostView

app_name = 'math'
urlpatterns = [
    path('', views.math_home_page, name='home-page'),
    path('create/', views.create, name='create'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
]