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

#User Registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login

def register(request):
    form = UserCreationForm()
    return render (request,"relationship_app/register.html")

#Set Up Role-Basef Views

from django.contrib.auth.decorators import user_passes_test
# Role check functions
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin, login_url='/login/')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@user_passes_test(is_librarian, login_url='/login/')
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@user_passes_test(is_member, login_url='/login/')
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

