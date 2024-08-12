from django.shortcuts import render , get_object_or_404

from .models import Book
# Create your views here.

def index(request):
    books = Book.objects.all()
    return render(request,"index.html",{
        "books":books
    })
def book_detail(request,slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request,"book_detail.html",{
        "slug":book.slug,
        "title":book.title,
        "author":book.author, 
        "rate":book.rate,
        "is_bestselling": book.is_bestselling,
        "description": book.description,
        "image": book.image
    })