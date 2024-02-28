from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(blank=True,upload_to="images/")
    folowers = models.ManyToManyField("self")


class Posts(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator")


class Followers(models.Model):
    folower = models.ManyToManyField()

