from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.DateField()


#Set Up the costom User model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    date_of_birth = models.DateField()
    profile_photo = models.ImageField()


# Create User Manage for Custom User Model

from django.contrib.auth.models import BaseUserManager

class CustomUSerManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        #create and return a regular user with an email and password
        if not email:
            raise ValueError("The email field must be set")
        
        email = self.normalize_email(email)

        user = self.model(email= email,**extra_fields)

        user.set_password(password)

        user.save(using=self._db)
        return user
    #create_superuser
    def create_superuser(self, email, password = None , **extra_fields):
        extra_fields.setdefault('is_user',True)
        extra_fields.setdefault('is_superuser',True)

        return self.create_user(email,password, **extra_fields)   