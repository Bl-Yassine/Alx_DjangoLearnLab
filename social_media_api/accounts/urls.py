from django.urls import path
from .views import user_login , register_user , ProfileView

urlpatterns = [
    path('register/', register_user , name ='register'),
    path('login/', user_login , name ='login'),
    path('profile/', ProfileView.as_view() , name ='profile'),
]