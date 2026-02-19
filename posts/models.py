from django.db import models

class Post(models.Model):
    instagram_id = models.CharField(max_length=50, unique=True)
    media_type = models.CharField(max_length=30)
    media_url = models.URLField()
    permalink = models.URLField()
    timestamp = models.DateTimeField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
