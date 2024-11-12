from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
# Create your views here.

def list_book(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')


class LibraryDetailView(DetailView):
    model =Library
    template_name ='relationship_app/library_detail.html'