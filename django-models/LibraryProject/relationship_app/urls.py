from django.urls import path
from . import views
from .views import list_books , register
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('ListBook/',views.list_books, name="list_book"),
    path('library_detail/', views.LibraryDetailView.as_view(),name="library_detail"),
    path('login/',LoginView.as_view(template_name='relationship_app/login.html', name='login')), #User Login
    path('logout/',LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),#User Logout
    path('register/',views.register, name='register'),#Register
    path('admin_view/', views.admin_view, name='admin_view'),
    path('librarian_view/', views.librarian_view, name='librarian_view'),
    path('member_view/', views.member_view, name='member_view'),
]