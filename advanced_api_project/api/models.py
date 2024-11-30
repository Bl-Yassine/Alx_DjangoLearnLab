from django.db import models
from datetime import date 
# Create your models here.

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

# Book model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

# Create Custom Serializers
from rest_framework import serializers

# Create BookSerializer
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__' #all fields

    def validate(self,publication_year):
        if (publication_year > date.today):
            raise serializers.ValidationError("the publication year should be in the present or in the past, not in the future")
        return publication_year

#Create AuthorSerializer
class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name'] #name field

