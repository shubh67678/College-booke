from django.urls import path
# from .views import BookDetailView
from . import views

urlpatterns = [
    path('', views.home, name="books-home"),
    path('book/<int:pk>/', views.detail, name="books-detail"),
    path('about/', views.about, name="books-about"),
    # path('book/<int:pk>/', BookDetailView.as_view(), name="books-detail"),
]
