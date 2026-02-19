from rest_framework import serializers
from posts.models import Post, Comment

class PostSerialiizer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"