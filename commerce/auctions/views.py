from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .util import *

import datetime



@login_required(login_url="/login")
def index(request):
    auctions = Auction.objects.all()

    auction_prices = {}

    final_contents = []

    for auction in auctions:
        auct_bids = Bid.objects.filter(auction=auction)
        if not auct_bids:
            continue
        else:
            time = get_latest_time(auct_bids)
            price = auct_bids.get(time=time)
            auction_prices[auction.id] = price

    for auct in auctions:
        d = {"product":auct.product,
             "id":auct.id,
             "time":auct.time,
             "image":auct.image,
             "description":auct.description,
             "category":auct.category,
             "price":auction_prices[auct.id].bid_price}
        final_contents.append(d)

    return render(request, "auctions/index.html",{
        "auctions":final_contents
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")



@login_required(login_url="/login")
def listings(request, listing_id):
    auction = Auction.objects.get(pk=listing_id)

    watchlist = Watchlist.objects.filter(auction=auction)

    for w in watchlist:
        if w.user == request.user:
            watchlisted = True

    bid_count = Bid.objects.filter(auction=auction)

    return render(request, "auctions/listing.html",{
        "auction":auction,
        "watchlist":watchlist
    })



@login_required(login_url="/login")
def categories(request):
    return render(request, "auctions/layout.html")



@login_required(login_url="/login")
def watchlist(request):
    return render(request, "auctions/layout.html")



@login_required(login_url="/login")
def create_listing(request):
    return render(request, "auctions/layout.html")
