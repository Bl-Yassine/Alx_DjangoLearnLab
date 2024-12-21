from django.shortcuts import render
from .models import Post , Comment
from .serializers import PostSerializers, CommentSerializers
from rest_framework.generics import ListAPIView , CreateAPIView ,RetrieveAPIView, UpdateAPIView ,DestroyAPIView
# Create your views here.

#Post-CreatView
class PostCreateView(CreateAPIView):
    serializer_class = PostSerializers

#Post-listView
class PostListView(ListAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

#Post-RetrieveView
class PostRetrieveView(RetrieveAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

#Post-UpdateView
class PostUpdateView(UpdateAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()

#Post-DeleteView
class PostDeleteView(DestroyAPIView):
    serializer_class = PostSerializers
    queryset = Post.objects.all()



#Comment-CreatView
class CommentCreateView(CreateAPIView):
    serializer_class = CommentSerializers

#Comment-listView
class CommentListView(ListAPIView):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

#Comment-RetrieveView
class CommentRetrieveView(RetrieveAPIView):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

#Comment-UpdateView
class CommentUpdateView(UpdateAPIView):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

#Comment-DeleteView
class CommentDeleteView(DestroyAPIView):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
