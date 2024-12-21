from django.shortcuts import render

# Create your views here.

#registerView
from .serializers import UserRegistationSerializers ,UserSerializer
from rest_framework import generics
from .models import CustomUser

class UserRegiterationView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserRegistationSerializers

# User Profile
from rest_framework import  permissions
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
