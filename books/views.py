from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import Post
from .models import book, book_type
# from django.views.generic import ListView

test_post = [
    {
        'name': 'book1',
        'price': '100',
        'description': 'test data',
        'date_posted': "10-1-10",
        'author': 'John Green',
        'user_id': '001',
        'book_type': 'fiction'

    },
    {
        'name': 'book2',
        'price': '100',
        'description': 'test2 data',
        'date_posted': "10-1-10",
        'author': 'Hank Green',
        'user_id': '002',
        'book_type': 'fiction'

    }
]


def home(request):
    context = {
        'books': book.objects.all()
    }
    return render(request, 'books/home.html', context)

# def


def about(request):
    return render(request, 'books/about.html', {'title': 'ABOUT'})
