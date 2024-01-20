from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    host_id = models.ForeignKey()
    current_bid_id = models.ForeignKey()
    product = models.CharField()
    description = models.CharField()
    image = models.ImageField()


class Bid(models.Model):
    user_id = models.ForeignKey()
    bid_price = models.IntegerField()
