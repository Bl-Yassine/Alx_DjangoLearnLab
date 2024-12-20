from django.db import models

# Create your models here.

#Create a custom user model use AbstractUser
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    bio = models.CharField(max_length=200)
    profile_picture=models.ImageField()
    followers=models.ManyToManyField('self',symmetrical=False)

    def __str__(self):
        return self.username

