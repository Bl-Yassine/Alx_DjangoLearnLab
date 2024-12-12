from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views
urlpatterns = [
    path('register/',views.RegisterUser.as_view() , name ='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]