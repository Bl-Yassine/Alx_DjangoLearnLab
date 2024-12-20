#Serializers for User Authentication 

from rest_framework import serializers
from .models import CustomUser

class UserSerializers(serializers.ModelSerializer):
    class Meta :
        model = CustomUser
        fields = ['username', 'email', 'password', 'bio', 'profile_picture']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = CustomUser(
                username=validated_data['username'],
                email=validated_data['email'],
                bio=validated_data.get('bio', ''),
                profile_picture=validated_data.get('profile_picture', None),
            )
            user.set_password(validated_data['password'])
            user.save()
            return user