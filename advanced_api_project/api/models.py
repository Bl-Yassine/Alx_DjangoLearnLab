from django.db import models

# Create your models here.

# Author model
class Author(models.Model):
    name = models.CharField(max_length=100)

# Book model
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)




