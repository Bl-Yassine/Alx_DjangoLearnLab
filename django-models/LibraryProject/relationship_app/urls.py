from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    path('ListBook/',views.list_books, name="list_book"),
    path('', views.LibraryDetailView.as_view(),name="library_detail"),
]