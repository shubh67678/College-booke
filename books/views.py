from django.shortcuts import render, get_object_or_404, redirect

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import book, book_type, request_book, transaction_confirmation
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
    ordering = ['-date_posted']
    paginate_by = 5


class UserBookListView(ListView):
    model = book
    template_name = 'books/user_books.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'book'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get(
            'username'))  # gets the username from url
        return book.objects.filter(user=user).order_by("price")


class BookDetailView(DetailView):
    model = book

    def post(self, request, *args, **kwargs):
        # if "approve_book" in request.POST:
        if "make_new_request" in request.POST:
            print(request.POST['make_new_request'])
            cur_book = self.get_object()
            new_request(cur_book, request)
        return redirect("books-home")

    def get_object(self):
        obj = super(BookDetailView, self).get_object(queryset=None)
        return obj


def new_request(book, request):
    cur_user = request.user
    # print(cur_user)
    temp_req = request_book(to_user=cur_user, needs_book=book)
    temp_req.save()


class IncomingRequestListView(ListView):
    model = request_book
    template_name = 'books/book_incoming_request.html'
    ordering = ['needs_book']


class IncomingRequestDetailView(DetailView):
    model = request_book

    def post(self, request, *args, **kwargs):
        if "approve_book" in request.POST:
            cur_request = self.get_object()
            # print("the curobject id", cur_obj)
            cur_request.request_status = not cur_request.request_status  # edit this xxx
            cur_request.save()
            new_transaction(cur_request.to_user, cur_request.needs_book)
            return redirect("user-request")

    def get_object(self):
        obj = super(IncomingRequestDetailView, self).get_object(queryset=None)
        return obj
 # def get_queryset(self):
 #     user = get_object_or_404(User, username=self.kwargs.get('username'))
 #     return request_book.objects.filter(needs_book.user == user).order_by("price")


def new_transaction(buying_user, buying_book, *arg):
    print(buying_book, buying_user)

    # print(transaction_confirmation.objects.all())
    if transaction_confirmation.objects.filter(bought_book=buying_book).first() == None:
        print(transaction_confirmation.objects.filter(bought_book=buying_book))
        print(transaction_confirmation.objects.filter(
            bought_book=buying_book).first())
        temp_transcation = transaction_confirmation(bought_book=buying_book)
        temp_transcation.save()
        delete_requested_book(buying_book)
        print("new transaction made")


def delete_requested_book(request_del):
    # while request_book.objects.filter(needs_book=request_del).first() !=None:
    request_book.objects.filter(needs_book=request_del).delete()


class UserRequestIncomingListView(ListView):
    model = request_book
    template_name = "books/user_request_incoming_list.html"

    def get_queryset(self):
        # gets the username from url
        cur_user = get_object_or_404(
            User, username=self.kwargs.get('requsername'))
        cur_user_books = book.objects.filter(user=cur_user)

        # joins and filters
        return request_book.objects.filter(needs_book__user=cur_user)


class UserRequestOutgoingListView(ListView):
    model = request_book
    template_name = "books/user_request_incoming_list.html"

    def get_queryset(self):
        cur_user = get_object_or_404(
            User, username=self.kwargs.get('requsername'))  # gets the username from url
        print('out', cur_user)

        # joins and filters
        return request_book.objects.filter(to_user=cur_user)


class TransactionCompletedListView(ListView):
    model = transaction_confirmation
    template_name = "books/transaction_confirmation_list.html"


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


def search(request):

    name = request.GET['book_search']

    a = book.objects.filter(name__contains=name)
    context = {
        "books": a,
        "search_book": name
    }
    return render(request, 'books/search.html', context)
    # return HttpResponse("hello whter")


def user_profile_links(request):

    context = {
        'user': request.user
    }
    return render(request, 'books/user_profile_to_links.html', context)
    # return HttpResponse("hello whter")


def about(request):
    return render(request, 'books/about.html', {'title': 'ABOUT'})


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
