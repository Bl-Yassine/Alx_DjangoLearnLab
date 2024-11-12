from django.urls import path
from .import views

urlpatterns = [
    path('ListBook/',views.list_book, name="list_book"),
    path('', views.LibraryDetailView.as_view(),name="library_detail"),
]