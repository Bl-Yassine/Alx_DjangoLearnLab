from django.db import models
from django.contrib.auth.models import User
from accounts.models import CustomUser
# Create your models here

#Post Model
class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
    

#Comment Model
class Comment(models.Model):
    post = models.ForeignKey(Post , on_delete=models.CASCADE)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now=True)





