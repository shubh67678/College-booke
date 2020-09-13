from django.urls import path
# from .views import BookDetailView
from django.contrib.auth import views as auth_views
from . import views
from users import views as users_views

urlpatterns = [
    path('', views.home, name="books-home"),
    path('book/<int:pk>/', views.detail, name="books-detail"),
    path('about/', views.about, name="books-about"),
    path('register/', users_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="logout"),
    path('profile/', users_views.profile, name="profile"),
    # path('book/<int:pk>/', BookDetailView.as_view(), name="books-detail"),
]
