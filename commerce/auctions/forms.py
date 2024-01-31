from django.forms import ModelForm, TextInput
from .models import Bid, Auction


class BidForm(ModelForm):
    class Meta:
        model = Bid
        fields = ["bid_price"]

class AuctionForm(ModelForm):
    class Meta:
        model = Auction
        exclude = ["host", "winner"]
        widgets = {
            "product": TextInput(),
            "description": TextInput(),
            "category": TextInput(),
            "image": Input(),
            "time":TextInput()
        }
