from django.db import models

# Create your models here.

#week11_task0
#creat simple model

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)

    