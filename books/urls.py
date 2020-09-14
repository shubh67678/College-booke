from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.home, name="books-home"),
    path('book/<int:pk>/', views.detail, name="books-detail"),
    path('about/', views.about, name="books-about"),
]
