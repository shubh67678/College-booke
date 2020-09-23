from django.contrib import admin
from .models import book, book_type, request_book, transaction_confirmation
# Register your models here.
admin.site.register(book)
admin.site.register(book_type)
admin.site.register(request_book)
admin.site.register(transaction_confirmation)
