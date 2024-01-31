from django.forms import ModelForm
from .models import Bid, Auction


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ["bid_price"]

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        exclude = ["host", "winner", ]
