from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as users_views
from . import views
from .views import (BookListView,
                    BookDetailView,
                    BookCreateView,
                    BookUpdateView,
                    BookDeleteView,
                    UserBookListView,
                    IncomingRequestListView,
                    IncomingRequestDetailView,
                    UserRequestIncomingListView,
                    UserRequestOutgoingListView,
                    TransactionCompletedListView
                    )
urlpatterns = [
    # path('', views.home, name="books-home"),
    path('', BookListView.as_view(), name="books-home"),
    path('user/<str:username>/', UserBookListView.as_view(), name="user-books"),
    # path('profilr/<str:username>/', UserBookListView.as_view(), name="user-books"),
    path('profile_links/', views.user_profile_links, name="user-profile-links"),
    path('request/', IncomingRequestListView.as_view(), name="user-request"),
    path('transactions/', TransactionCompletedListView.as_view(),
         name="user-sold-books"),
    path('request/<int:pk>', IncomingRequestDetailView.as_view(),
         name="request-detail"),
    path('request_in/<str:requsername>/', UserRequestIncomingListView.as_view(),
         name="user-request-incoming"),
    path('request_out/<str:requsername>/', UserRequestOutgoingListView.as_view(),
         name="user-request-outgoing"),
    path('book/<int:pk>/', BookDetailView.as_view(), name="books-detail"),
    path('book/search/', views.search, name="books-search"),
    path('book/new/', BookCreateView.as_view(), name="books-create"),
    path('book/<int:pk>/update/', BookUpdateView.as_view(), name="books-update"),
    path('book/<int:pk>/delete/', BookDeleteView.as_view(), name="books-delete"),
    # path('about/', views.about, name="books-about"),
]
