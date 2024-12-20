from django.shortcuts import render

# Create your views here.

#Registering Users

from rest_framework import status, permissions , generics ,viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializers

@api_view(['POST'])
def register_user(request):
    if request.method == 'POST':
        serializer = UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

#User Login with Authentication Toikens 


from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from django.core.exceptions import ObjectDoesNotExist

from .models import CustomUser

@api_view(['POST'])
def user_login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if '@' in username:
            try :
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass
            if not user :
                user = authenticate(username = username , password = password)
            if user :
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token' : token.key}, status= status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

#profile View
class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializers
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


