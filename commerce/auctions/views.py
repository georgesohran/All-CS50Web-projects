from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from .util import *

import datetime
utc=pytz.UTC


@login_required(login_url="/login")
def index(request, category=None):
    if not category:
        auctions = Auction.objects.all()
    else:
        auctions = Auction.objects.filter(category=category)

    final_contents = []
    for auct in auctions:
        auct_bids = Bid.objects.filter(auction=auct)

        closed = False
        if auct.winner:
            closed = True

        if not auct_bids:
            price = 0
        else:
            price = auct_bids.filter(time=get_latest_time(auct_bids))[0].bid_price

        d = {"product":auct.product,
             "id":auct.id,
             "time":auct.time,
             "image":auct.image,
             "description":auct.description,
             "category":auct.category,
             "price":price,
             "closed":closed,
             "winner":auct.winner,
             "messege":None}
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

    #checking if the current user is the host
    is_host = False
    if auction.host == request.user:
        is_host = True

    #checking if current user have watchlisted it
    watchlisted = False
    for w in watchlist:
        if w.user == request.user:
            watchlisted = True
            break

    #getting number of nids and current price of the pruduct, by filtering for the latest bid
    bids = Bid.objects.filter(auction=auction)
    bid_count = bids.count()

    #checking wether this auction has any bids or not
    if not bids.filter(time=get_latest_time(bids)):
        price = 0
    else:
        price = bids.get(time=get_latest_time(bids)).bid_price

    comments = Comment.objects.filter(auction=auction)

    current_user_is_winner = False
    if request.user == auction.winner:
        current_user_is_winner = True

    form = BidForm()

    if request.method == "POST":
        #if the user is trying to close an auction
        if "close" in request.POST and is_host:
            winner = bids.get(time=get_latest_time(bids)).user
            auction.winner = winner
            auction.save()
            return HttpResponseRedirect(reverse("index"))

        #if user presses the watchlist button adding him to watchlisted users
        if "wlist" in request.POST:
            new_watchlist = Watchlist(auction=auction, user=request.user)
            new_watchlist.save()
            return render(request, "auctions/listing.html",{
                "auction":auction,
                "watchlist":watchlist,
                "bid_count":bid_count,
                "watchlisted":watchlisted,
                "price":price,
                "form":form,
                "is_host":is_host,
                "winner":auction.winner,
                "comments":comments,
                "is_winner":current_user_is_winner,
            })

        #if the user tries to write a comment we save it
        if "comment" in request.POST:
            new_comment = Comment(auction=auction, user=request.user)
            new_comment.contents = request.POST["contents"]
            new_comment.save()
            return render(request, "auctions/listing.html",{
                "auction":auction,
                "watchlist":watchlist,
                "bid_count":bid_count,
                "watchlisted":watchlisted,
                "price":price,
                "form":form,
                "is_host":is_host,
                "winner":auction.winner,
                "comments":comments,
                "is_winner":current_user_is_winner,
            })

        bid = Bid(auction=auction, user=request.user, time = datetime.datetime.now())
        form = BidForm(request.POST, instance=bid)

        if form.is_valid():
            if float(request.POST["bid_price"]) < price:
                return render(request, "auctions/listing.html",{
                    "auction":auction,
                    "watchlist":watchlist,
                    "bid_count":bid_count,
                    "watchlisted":watchlisted,
                    "price":price,
                    "form":form,
                    "is_host":is_host,
                    "winner":auction.winner,
                    "comments":comments,
                    "is_winner":current_user_is_winner,
                    "messege":"Invalid bid"
                    })
            else:
                form.save()
                return HttpResponseRedirect(reverse("index"))

        return HttpResponseRedirect(reverse("index"))

    else:

        return render(request, "auctions/listing.html",{
            "auction":auction,
            "watchlist":watchlist,
            "bid_count":bid_count,
            "watchlisted":watchlisted,
            "price":price,
            "form":form,
            "is_host":is_host,
            "winner":auction.winner,
            "comments":comments,
            "is_winner":current_user_is_winner,
        })



@login_required(login_url="/login")
def categories(request):
    if request.method == "POST":
        cat = request.POST["category"]
        return HttpResponseRedirect(reverse("index_cat", args=(cat,)))
    else:
        auctions = Auction.objects.all()
        categor = []
        for auction in auctions:
            categor.append(auction.category)
        categor = set(categor)

        return render(request, "auctions/categories.html", {
            "categories":categor,
            })



@login_required(login_url="/login")
def watchlist(request):
    wlist = Watchlist.objects.filter(user=request.user)

    auctions = []
    for wl in wlist:
        auctions.append(wl.auction)

    final_contents = []
    for auct in auctions:
        auct_bids = Bid.objects.filter(auction=auct)

        closed = False
        if auct.winner:
            closed = True

        if not auct_bids:
            price = 0
        else:
            price = auct_bids.filter(time=get_latest_time(auct_bids))[0].bid_price
        d = {"product":auct.product,
             "id":auct.id,
             "time":auct.time,
             "image":auct.image,
             "description":auct.description,
             "category":auct.category,
             "price":price,
             "closed":closed,
             "winner":auct.winner,
             "messege":None}
        final_contents.append(d)

    return render(request, "auctions/watchlist.html",{
        "auctions":final_contents
    })



@login_required(login_url="/login")
def create_listing(request):
    if request.method == "POST":
        ...
    else:

        return render(request, "auctions/create_listing.html")
