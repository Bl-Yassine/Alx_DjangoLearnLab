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
    #Roles
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
    #permission_required
    path('add_book',views.add_book,name="add_book"),
    path('edit_book',views.change_book,name="edit_book"),
    path('delete_book',views.change_book,name="delete_book"),
]