from rest_framework import serializers
from .models import Book, Author
from django.utils.timezone import now

# Create BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' #all fields


#Create AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = ['name'] #name field