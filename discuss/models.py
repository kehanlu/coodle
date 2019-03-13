from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post')
    title = models.CharField(max_length=200)
    content = models.TextField()  # markdown string
    create_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment')
    content = models.TextField()  # markdown
    create_date = models.DateTimeField(auto_now_add=True)
