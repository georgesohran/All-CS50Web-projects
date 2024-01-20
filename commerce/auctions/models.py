from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Bid(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    bid_price = models.IntegerField()


class Auction(models.Model):
    host_id = models.ForeignKey(User, models.CASCADE)
    # current_bid_id = models.ForeignKey(Bid, models.CASCADE)
    product = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    image = models.ImageField(blank=True)
    time = models.CharField()


class Auction_Bids(models.Model):
    auction_id = models.ForeignKey(Auction, models.CASCADE)
    bid_id = models.ForeignKey(Bid, models.CASCADE)



