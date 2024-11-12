from django.shortcuts import render
from .models import Book,Library
from django.views.generic import DetailView
# Create your views here.

def list_book(request):
    books = Book.objects.all()
    return render(request, 'list_books.html')


class LibraryDetailView(DetailView):
    model =Library
    template_name ='library_detail.html'