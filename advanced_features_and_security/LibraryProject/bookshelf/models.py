from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()


#Set Up the costom User model
from django.contrib.auth.models import AbstractUser

class CostumUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()
    