from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#create Post Model
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.CharField(max_length=200,default="")

    def __str__(self):
        return self.title

#create Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

#Tag model:
class Tag(models.Model):
    name = models.CharField(max_length=50)
    post = models.ManyToManyField(Post)

    def __str__(self):
        return self.name



