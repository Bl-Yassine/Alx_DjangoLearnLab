from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.apiOverview, name="api_OverView"),
    path("book_list/", views.ListView, name="ListView"),
    path("book_detail/<str:pk>/", views.DetailView, name="DetailView"),
    path("book_create/", views.CreateView, name="CreateView"),
    path("book_update/<str:pk>/", views.UpdateView, name="UpdateView"),
    path("book_delete/<str:pk>/", views.DeleteView, name="DeleteView"),

]