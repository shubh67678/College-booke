from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views
from . import views
from .views import BookListView, BookDetailView
urlpatterns = [
    # path('', views.home, name="books-home"),
    path('', BookListView.as_view(), name="books-home"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="books-detail"),
    # path('about/', views.about, name="books-about"),
]
