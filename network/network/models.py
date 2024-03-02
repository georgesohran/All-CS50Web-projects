from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(blank=True,upload_to="images/")
    followers = models.ManyToManyField("self", blank=True, null=True)

    def __str__(self):
        return f"{self.email}"


class Posts(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator_post")
    timestamp = models.DateTimeField()
    body = models.CharField(max_length=1024)
    title = models.CharField(max_length=64)
    likes = models.IntegerField()
    dislikes = models.IntegerField()

    def __str__(self):
        return f"{self.creator}, {self.title} : {self.timestamp}"


class Comments(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator_comment")
    commented_post = models.ForeignKey(User, models.CASCADE, related_name="commented_post")
    body = models.CharField(max_length=1024)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    timestamp = models.DateTimeField()

    def __str__(self):
        return f"{self.creator} : {self.timestamp}"


