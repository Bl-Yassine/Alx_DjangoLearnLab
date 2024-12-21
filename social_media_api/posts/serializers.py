from rest_framework import serializers
from .models import Post , Comment

#Post Serializers
class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

#  Comment Serializers 
class CommentSerializers(serializers.ModelField):
    class Meta:
        model = Comment
        fields = '__all__'