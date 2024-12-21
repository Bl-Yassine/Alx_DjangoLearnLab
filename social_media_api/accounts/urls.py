from django.urls import path
from .views import UserRegiterationView , ProfileView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('register/', UserRegiterationView.as_view() , name ='register'),
    path('login/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('profile/', ProfileView.as_view(), name='user-profile'),
]