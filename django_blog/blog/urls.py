from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from blog import views

urlpatterns = [
    path('',views.basepage, name ='home'),
    path('register/',views.registeruser, name ='register'),
    path('login/', LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', views.profileinfo, name='profile'),
    path('editprofile/', views.editProfile, name='edit'),
    path('post/',views.PostListiView.as_view(),name='posts'),
    path('post/new/',views.PostCreateView.as_view(),name='postcreate'),
    path('post/<int:pk>/',views.PostDetailView.as_view(),name='postdetail'),
    path('post/<int:pk>/update/',views.PostUpdateView.as_view(),name='postupdate'),
    path('post/<int:pk>/delete/',views.PostDeleteView.as_view(),name='postdelete'),
    path('post/<int:pk>/comments/',views.CommentListiView.as_view(),name='postandcomment'), #Comment List View
    path('post/<int:pk>/comments/<int:pk>/',views.CommentDetailView.as_view(),name='Commentdetai'), # Comment Detail View
    path('post/<int:pk>/comments/new/',views.CommentCreateView.as_view(),name='CreateComment'), # Comment Create View
    path('post/<int:pk>/comment/<int:pk>/update/',views.CommentUpdateView.as_view(),name='updateComment'), # Comment Update View
    path('post/<int:pk>/comment/<int:pk>/delete/',views.PostDeleteView.as_view(),name='deleteComment'), # Comment Delete View
    path('tags/<str:tag_name>/', views.PostListiView.as_view(), name='posts_by_tag'),
    path('search/', views.PostListiView.as_view(), name='post_search'),
]