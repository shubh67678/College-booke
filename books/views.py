from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# from .models import Post

test_post = [
    {
        'title': 'a2',
        'content': 'addd',
        'date_posted': "10-1-10",
        'author': 'user 1'

    },
    {
        'title': 'b3',
        'content': 'sub',
        'date_posted': "9-3-9",
        'author': 'user 3'

    }
]


def home(request):
    context = {
        # 'posts': Post.objects.all()
        'posts': test_post
    }
    return render(request, 'books/home.html', context)


def about(request):
    return render(request, 'books/about.html', {'title': 'ABOUT'})
