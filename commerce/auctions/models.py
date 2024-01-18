from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Auction(models.Model):
    user_id = models.ForeignKey()



class Bid(models.Model):
    pass
