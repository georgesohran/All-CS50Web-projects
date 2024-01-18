from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    product = models.CharField()
    description = models.CharField()
    


class Bid(models.Model):
    user_id = models.ForeignKey()
    bid_price = models.IntegerField()
