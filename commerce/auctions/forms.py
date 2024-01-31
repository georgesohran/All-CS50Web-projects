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
        #widgets = {
        #    "product": TextInput(attrs={}),
        #    "description": TextInput(attrs={}),
        #    "category": TextInput(attrs={}),
        #    "image": FileInput(attrs={}),
        #}
