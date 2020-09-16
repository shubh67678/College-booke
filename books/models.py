from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class book(models.Model):
    name = models.CharField(max_length=100)
    price = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=100)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("books-detail", kwargs={"pk": self.pk})


class book_type(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    book_type = models.CharField(max_length=50)
