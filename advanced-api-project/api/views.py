from django.shortcuts import render

# Create your views here.

#ListView for retrieving all books.
from rest_framework import generics
from .models import Book ,Author
from .serializers import BookSerializer ,AuthorSerializer

#Permission

from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated ,IsAuthenticated



#Set Up Generic Views
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

@api_view(['GET'])
def apiOverview(request):
    api_url = {
        'ListView':'/book_list/',
        'DetailView':'/book_detail/<str:pk>/',
        'CreateView':'/book_create/',
        'UpdateView':'/book_update/<str:pk>/',
        'DeleteView':'/book_delete/<str:pk>/',
    }
    return Response(api_url)

#ListView
@api_view(['GET'])
def ListView(request):
    books = Book.objects.all()
    serializer = BookSerializer(books , many=True)
    filter_backend = [DjangoFilterBackend, filters.SearchFilter , filters.OrderingFilter ] #filter, search , ordoring
    filterset_fields = ['title','publication_year','author'] #filter
    search_fields = ['title','publication_year','author'] #search
    ordering_fields = ['title','publication_year','author'] #Ordering
    return Response(serializer.data)

#DetailView 
@api_view(['GET'])
def DetailView(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(books , many=False)
    return Response(serializer.data)

#CreateView 
@api_view(['POST'])
def CreateView(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#UpdateView 
@api_view(['POST'])
def UpdateView(request, pk):
    books = Book.objects.get(id=pk)
    serializer = BookSerializer(isinstance= books ,data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

#DeleteView  
@api_view(['DELETE'])
def DeleteView(request, pk):
    books = Book.objects.get(id=pk)
    books.delete()
    return Response("Succesfully delete!")