from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    host = models.ForeignKey(User, models.CASCADE)
    product = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    category = models.CharField(max_length=64, blank=True)
    image = models.ImageField(blank=True)
    time = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return f"host: {self.host_id},\nproduct: {self.product},\ntime: {self.time}"


class Bid(models.Model):
    auction = models.ForeignKey(Auction, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    time = models.DateTimeField()
    bid_price = models.IntegerField()

    def __str__(self):
        return f"user: {self.user_id},\nbid_price: {self.bid_price}"


class Comment(models.Model):
    auction = models.ForeignKey(Auction, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    contents = models.CharField(max_length=1024)

    def __str__(self):
        return f"user: {self.user_id},\ncontents: {self.contents},\nauction: {self.auction_id}"


class Watchlist(models.Model):
    auction = models.ForeignKey(Auction, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"user: {self.user_id},\nauction: {self.auction_id}"

