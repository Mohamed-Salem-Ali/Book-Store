from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'rate', 'is_bestselling')
    prepopulated_fields = {'slug': ('title',)}