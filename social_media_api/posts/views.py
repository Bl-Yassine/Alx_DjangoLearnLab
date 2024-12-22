from django.shortcuts import render
from .models import Post , Comment
from .serializers import PostSerializers, CommentSerializers
from rest_framework import viewsets
# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers


