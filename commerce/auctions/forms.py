from django.forms import ModelForm, TextInput, FileInput
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
            "product": TextInput(attrs={"style":"text-align:center"}),
            "description": TextInput(attrs={"style":"text-align:center"}),
            "category": TextInput(attrs={"style":"text-align:center"}),
            "image": FileInput(attrs={"style":"text-align:center"}),
        }
