from django.db import models
from django.contrib.auth.models import User


class Problem(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='problem')
    title = models.CharField(max_length=200)
    description = models.TextField()
    short_description = models.TextField(blank=True)
    sample_code = models.TextField(blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Submission(models.Model):
    problem = models.ForeignKey(
        Problem, on_delete=models.CASCADE, related_name='psub')  # problem submission
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='usub')  # user submission
    code = models.TextField()
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} | {}'.format(self.problem.title, self.user.profile.nickname)
