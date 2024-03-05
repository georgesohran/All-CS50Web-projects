from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core.paginator import Paginator
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from itertools import chain
from operator import attrgetter

from .models import *



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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def index(request):
    posts = Post.objects.all().exclude(creator=request.user).order_by("-timestamp")
    return render(request, "network/index.html", {
        "posts":posts
    })


@login_required(login_url="/login")
def following(request):
    if request.method == "GET":
        user = User.objects.get(id=request.user.id)
        posts = []

        for followed in user.followers.all():
            p = Post.objects.filter(creator=followed)
            posts.append(p)

        final_posts = sorted(
            chain(*posts),
            key=attrgetter("timestamp"),
            reverse=True
        )

        return render(request, "network/following.html", {
            "posts": final_posts
        })

    else:
        return render(request, "network/following.html", {
            "posts": final_posts
        })


@login_required(login_url="/login")
def profile(request, id):
    see_user = User.objects.get(id=id)
    posts = Post.objects.filter(creator=see_user)
    return render(request, "network/profile.html", {
        "see_user":see_user,
        "posts":posts
    })

# API routes are here:

@csrf_exempt
@login_required
def api_make_post(request):
    if request.method == "POST":
        contents = request.POST["contents"]
        if not contents:
            return JsonResponse({"message":"insert your content first"})

        try:
            new_post = Post(body=contents, creator=request.user)
            new_post.save()
        except IntegrityError:
            return JsonResponse({"message":"something went wrong..."})

        return JsonResponse({"message":"ok"})
    else:
        return JsonResponse({"message":"invalid request"})
