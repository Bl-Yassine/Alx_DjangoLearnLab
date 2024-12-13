from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
urlpatterns = [
    path('',views.basepage, name ='home'),
    path('register/',views.registeruser, name ='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profileinfo, name='profile'),
    path('editprofile/', views.editProfile, name='edit'),
    path('posts/',views.PostListiView.as_view(),name='posts'),
    path('createpost/',views.PostCreateView.as_view(),name='postcreate'),
    path('posts/<int:pk>/',views.PostDetailView.as_view(),name='postdetail'),
    path('posts/<int:pk>/update',views.PostUpdateView.as_view(),name='postupdate'),
    path('posts/<int:pk>/delete',views.PostDeleteView.as_view(),name='postdelete'),
]