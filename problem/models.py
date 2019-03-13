from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='problem')
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.TextField()
    sample_code = models.TextField()
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)


class Submission(models.Model):
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name='psub')  # problem submission
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usub')  # user submission
    code = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)
