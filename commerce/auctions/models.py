from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    host = models.ForeignKey(User, models.CASCADE, related_name="host")
    winner = models.ForeignKey(User, models.CASCADE, related_name="winner")
    product = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
    category = models.CharField(max_length=64, blank=True)
    image = models.ImageField(blank=True,upload_to="images/")
    time = models.DateTimeField()

    def __str__(self):
        return f"host: {self.host_id},product: {self.product},time: {self.time}"


class Bid(models.Model):
    auction = models.ForeignKey(Auction, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    time = models.DateTimeField()
    bid_price = models.FloatField()

    def __str__(self):
        return f"user: {self.user_id},bid_price: {self.bid_price}"


class Comment(models.Model):
    auction = models.ForeignKey(Auction, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)
    contents = models.CharField(max_length=1024)

    def __str__(self):
        return f"user: {self.user_id},contents: {self.contents},auction: {self.auction_id}"


class Watchlist(models.Model):
    auction = models.ForeignKey(Auction, models.CASCADE)
    user = models.ForeignKey(User, models.CASCADE)

    def __str__(self):
        return f"user: {self.user_id},auction: {self.auction_id}"

