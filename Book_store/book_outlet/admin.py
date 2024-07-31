from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rate', 'is_bestselling')
    fields = ('title', 'author', 'rate', 'is_bestselling', 'description')

admin.site.register(Book, BookAdmin)