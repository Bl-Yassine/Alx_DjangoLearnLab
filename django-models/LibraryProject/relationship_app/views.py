from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView

# Create your views here.

#Create a function-based view in relationship_app/views.py that lists all books stored in the database.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html')

#Create a class-based view in relationship_app/views.py that displays details for a specific library, listing all books available in that library.
class LibraryDetailView(DetailView):
    model =Library
    template_name ='relationship_app/library_detail.html'





