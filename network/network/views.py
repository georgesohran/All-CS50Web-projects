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
import json

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
    context = []
    posts = Post.objects.all().order_by("-timestamp")
    for post in posts:
        likes = Like.objects.filter(liked_post=post)
        likes_num = likes.count()

        user_like = True
        if not likes.filter(user=request.user):
            user_like = False

        comments = Comment.objects.filter(commented_post=post)
        d = {"post":post, "comments":comments, "likes_num":likes_num, "user_like":user_like}
        context.append(d)

    return render(request, "network/index.html", {
        "posts":context
    })


@login_required(login_url="/login")
def following(request):
    context = []
    user = User.objects.get(id=request.user.id)
    posts = []

    for followed in user.followers.all():
        p = Post.objects.filter(creator=followed)
        posts.append(p)

    posts = sorted(
        chain(*posts),
        key=attrgetter("timestamp"),
        reverse=True
    )

    for post in posts:
        likes = Like.objects.filter(liked_post=post)
        likes_num = likes.count()

        user_like = True
        if not likes.filter(user=request.user):
            user_like = False

        comments = Comment.objects.filter(commented_post=post)
        d = {"post":post, "comments":comments, "likes_num":likes_num, "user_like":user_like}
        context.append(d)

    return render(request, "network/following.html", {
        "posts": context
    })


@login_required(login_url="/login")
def profile(request, id):
    see_user = User.objects.get(id=id)
    posts = Post.objects.filter(creator=see_user)

    full_posts_data = []

    for post in posts:
        likes = Like.objects.filter(liked_post=post)
        likes_num = likes.count()

        user_like = True
        if not likes.filter(user=request.user):
            user_like = False

        comments = Comment.objects.filter(commented_post=post)
        d = {"post":post, "comments":comments, "likes_num":likes_num, "user_like":user_like}
        full_posts_data.append(d)

    return render(request, "network/profile.html", {
        "see_user":see_user,
        "posts":full_posts_data
    })

# API routes are here:

@csrf_exempt
@login_required
def api_make_post(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if not data.get("contents"):
            return JsonResponse({"message":"insert your content first"})

        contents = data.get("contents")
        try:
            new_post = Post(body=contents, creator=request.user)
            new_post.save()
        except IntegrityError:
            return JsonResponse({"message":"something went wrong..."})

        return JsonResponse({"message":"making a new post was successful"})

    elif request.method == "PUT":
        #basicly eddit post
        return JsonResponse({"message":"work in progress..."})

    else:
        return JsonResponse({"message":"invalid request"})

@csrf_exempt
@login_required
def api_make_comment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        if not data.get("contents"):
            return JsonResponse({"message":"insert your comment first"})

        if not data.get("commented_post_id"):
            return JsonResponse({"message":"How did you create a comment without a post id?"})

        contents = data.get("contents")
        post_id = data.get("commented_post_id")
        try:
            commented_post = Post.objects.get(id=post_id)
            comment = Comment(body=contents, creator=request.user, commented_post=commented_post)
            comment.save()
        except IntegrityError:
            return JsonResponse({"message":"something went wrong..."})

        return JsonResponse({"message":"making a comment was successful",
                             "comment":{"creator":comment.creator.username,
                                        "timestamp":comment.timestamp,
                                        "body":comment.body}
                            })

    else:
        return JsonResponse({"message":"invalid request"})


@csrf_exempt
@login_required
def api_like(request, post_id):
    if request.method != "POST":
        return JsonResponse({"message":"wrong request method"})
    try:
        post = Post.objects.get(id=post_id)
    except IntegrityError:
        return JsonResponse({"message":"invalid post id"})

    user_like = Like.objects.filter(user=request.user, liked_post=post)

    if user_like:
        user_like[0].delete()
        total_likes = Like.objects.filter(liked_post=post).count()
        return JsonResponse({"message":"unliked this post successfuly!", "likes":total_likes, "user_like":False})
    else:
        like = Like(user=request.user, liked_post=post)
        like.save()
        total_likes = Like.objects.filter(liked_post=post).count()
        return JsonResponse({"message":"liked this post successfuly!","likes":total_likes, "user_like":True})


@csrf_exempt
@login_required
def api_edit(request, post_id):
    return JsonResponse()
