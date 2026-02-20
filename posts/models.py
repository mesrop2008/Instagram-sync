from django.db import models

class Post(models.Model):
    instagram_id = models.CharField(max_length=200, unique=True)
    media_type = models.CharField(max_length=200)
    media_url = models.URLField(max_length=999)
    permalink = models.URLField(max_length=1000)
    timestamp = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
