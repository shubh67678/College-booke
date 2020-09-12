from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import Post
from .models import book, book_type
from django.views.generic import ListView, DetailView

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
        'books': book.objects.all(),
        'books_type': book_type.objects.all()
    }
    return render(request, 'books/home.html', context)


# class BookListView(ListView):
#     model = book
    # template_name = "books/home.html"
    # context_object_name = "books"


# class BookDetailView(DetailView):
#     model = book

def detail(request, *args, **kwargs):
    primary_key = kwargs['pk']
    a = book_type.objects.filter(book_id=primary_key)

    context = {
        'books': book.objects.filter(pk=primary_key),
        'book_type': a
    }

    return render(request, 'books/detail.html', context)


# class BookDetailView(DetailView):
#     model = book_type.objects.filter(pk=pk)


def about(request):
    return render(request, 'books/about.html', {'title': 'ABOUT'})
