from django.urls import path
from . import views
urlpatterns = [
    path("api/books", views.BookListCreateAPIView.as_view(), name="book_list"),
    path("api/authors", views.AuthorListCreateAPIView.as_view(), name="book_list"),
]