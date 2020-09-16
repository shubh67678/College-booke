from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views
from . import views
from .views import (BookListView, BookDetailView,
                    BookCreateView, BookUpdateView, BookDeleteView, UserBookListView)
urlpatterns = [
    # path('', views.home, name="books-home"),
    path('', BookListView.as_view(), name="books-home"),
    path('user/<str:username>', UserBookListView.as_view(), name="user-books"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="books-detail"),
    path('book/new/', BookCreateView.as_view(), name="books-create"),
    path('book/<int:pk>/update', BookUpdateView.as_view(), name="books-update"),
    path('book/<int:pk>/delete', BookDeleteView.as_view(), name="books-delete"),
    # path('about/', views.about, name="books-about"),
]
