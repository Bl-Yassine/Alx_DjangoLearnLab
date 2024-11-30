from rest_framework import serializers
from .models import Book, Author
from django.utils.timezone import now

# Create BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' #all fields

    def validate(self,publication_year):
            if (publication_year > now().year):
                raise serializers.ValidationError("the publication year should be in the present or in the past, not in the future")
            return publication_year

#Create AuthorSerializer
class AuthorSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = Author
        fields = '__all__'