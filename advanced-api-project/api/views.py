from django.shortcuts import render

# Create your views here.

#ListView for retrieving all books.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

class CustomBookListView(generics.ListAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer





