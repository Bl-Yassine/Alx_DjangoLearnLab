from django.urls import path
from . import views
from views import list_book
from views import LibraryDetailView

urlpatterns = [
    path('ListBook/',views.list_book, name="list_book"),
    path('', views.LibraryDetailView.as_view(),name="library_detail"),
]