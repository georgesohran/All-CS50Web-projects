from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    followers = models.ManyToManyField("self", blank=True, null=True)
    about_me = models.TextField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f"{self.username}"


class Post(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator_post")
    image = models.ImageField(blank=True, null=True, upload_to="images/")
    body = models.TextField(max_length=1024)
    likes = models.IntegerField(default=0)
    edited = models.BooleanField(initial=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator}, {self.body}, {self.timestamp}"


class Comment(models.Model):
    creator = models.ForeignKey(User, models.CASCADE, related_name="creator_comment")
    commented_post = models.ForeignKey(Post, models.CASCADE, related_name="commented_post")
    body = models.TextField(max_length=1024)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.creator} : {self.timestamp}"

class Like(models.Model):
    user = models.ForeignKey(User, models.CASCADE, related_name="like")
    liked_post = models.ForeignKey(Post, models.CASCADE, related_name="liked_post")
