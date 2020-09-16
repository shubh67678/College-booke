from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import book, book_type
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    UpdateView
)

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


class BookListView(ListView):
    model = book
    template_name = 'books/home2.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'book'
    # ordering = ['-date_posted']
    paginate_by = 5


class UserBookListView(ListView):
    model = book
    template_name = 'books/user_books.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'book'
    # ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return book.objects.filter(user=user).order_by("price")


class BookDetailView(DetailView):
    model = book


class BookCreateView(LoginRequiredMixin, CreateView):
    model = book
    fields = ['name', 'description', 'price', 'author']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = book
    fields = ['name', 'description', 'price', 'author']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        return False


class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = book
    success_url = '/'

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        return False


# def detail(request, *args, **kwargs):
#     primary_key = kwargs['pk']
#     a = book_type.objects.filter(book_id=primary_key)

#     context = {
#         'books': book.objects.filter(pk=primary_key),
#         'book_type': a
#     }

#     return render(request, 'books/detail.html', context)


# class BookDetailView(DetailView):
#     model = book_type.objects.filter(pk=pk)


def about(request):
    return render(request, 'books/about.html', {'title': 'ABOUT'})
