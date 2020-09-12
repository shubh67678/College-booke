from django.urls import path
from .views import BookListView
from . import views

urlpatterns = [
    path('', views.home, name="books-home"),
    path('about/', views.about, name="books-about"),
]
