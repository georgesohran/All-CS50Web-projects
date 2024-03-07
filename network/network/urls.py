from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("following", views.following, name="following"),
    path("profile/<int:id>", views.profile, name="profile"),
    #API rputes
    path("api_make_post", views.api_make_post, name="make_post"),
    path("api_make_comment", views.api_make_comment, name="make_comment"),
    path("api_like/<int:post_id>", views.api_like, name="like")
]
