from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.apiOverview, name="api_OverView"),
    path("books/", views.ListView, name="ListView"),
    path("book_detail/<str:pk>/", views.DetailView, name="DetailView"),
    path("books/create/", views.CreateView, name="CreateView"),
    path("books/update/<str:pk>/", views.UpdateView, name="UpdateView"),
    path("bbooks/delete/<str:pk>/", views.DeleteView, name="DeleteView"),

]