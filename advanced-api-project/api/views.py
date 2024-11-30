from django.shortcuts import render

# Create your views here.

#ListView for retrieving all books.
from rest_framework import generics
from .models import Book ,Author
from .serializers import BookSerializer ,AuthorSerializer

#Book Views

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



