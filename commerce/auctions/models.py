from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bid(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    bid_price = models.IntegerField()


class Auction(models.Model):
    host_id = models.ForeignKey(User, models.CASCADE)
    current_bid_id = models.ForeignKey(Bid, models.CASCADE)
    product = models.CharField()
    description = models.CharField()
    image = models.ImageField()


