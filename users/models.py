from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    point = models.IntegerField(default=0)
    nickname = models.CharField(max_length=200)

    def __str__(self):
        return "{}".format(self.nickname)
