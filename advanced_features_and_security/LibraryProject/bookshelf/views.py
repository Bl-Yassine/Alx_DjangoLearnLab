from django.shortcuts import render

# Create your views here.
#Create groupe 
from django.contrib.auth.models import Group , Permission
from django.contrib.contenttypes.models import ContentType
from .models import CustomUser

from django.contrib.auth.decorators import permission_required
from .models import Book
@permission_required('bookshelf.can_view', raise_exception=True)  # Ensure the user has 'can_view' permission
def book_list(request):
    """
    A view to display a list of books, accessible only to users with the 'can_view' permission.
    """
    books = Book.objects.all()  # Retrieve all book objects
    return render(request, 'books/book_list.html', {'books': books})  # Pass books to the template