from django.forms import ModelForm, TextInput, FileInput, Textarea
from .models import Bid, Auction


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ["bid_price"]

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        exclude = ["host", "winner", "time"]
        widgets = {
            "product": TextInput(attrs={"size":"60"}),
            "description": Textarea(attrs={"cols":"63"}),
            "category": TextInput(attrs={"size":"60"}),
            "image": FileInput(attrs={}),
        }
