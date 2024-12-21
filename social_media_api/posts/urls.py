from django.urls import path 
from . import views

urlpatterns = [

    #Post CRUD URLS
    path('post/',views.PostListView.as_view(), name='list_post'),
    path('post/create/',views.PostCreateView.as_view(), name='create_post'),
    path('post/<int:pk>/',views.PostRetrieveView.as_view(), name='retrieve_post'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(), name='delete_post'),

    #Comment CRUD URLS
    path('Comment/',views.CommentListView.as_view(), name='comment_post'),
    path('Comment/create/',views.CommentCreateView.as_view(), name='comment_post'),
    path('Comment/<int:pk>/',views.CommentRetrieveView.as_view(), name='comment_post'),
    path('Comment/<int:pk>/update/',views.CommentUpdateView.as_view(), name='comment_post'),
    path('Comment/<int:pk>/delete/',views.CommentDeleteView.as_view(), name='comment_post'),
]
