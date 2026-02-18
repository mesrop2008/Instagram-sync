from django.db import models

class Post(models.Model):
    id = models.CharField(max_length=50, unique=True)
    media_type = models.CharField(max_length=30)
    media_url = models.URLField()
    perma_link = models.URLField()
    timestamp = models.DateTimeField()


class Comment(models.model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)