from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(blank=True,upload_to="images/")
    folowers = models.ManyToManyField("self")


class Posts(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator")
    timestamp = models.DateTimeField()
    body = models.CharField()
    title = models.CharField()


class Comments(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator")
    commented_post = models.ForeignKey(User, models.CASCADE, related_name="com_post")
    contents = models.CharField()
    



