from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entry, name="entry")
    path("search_results", views.search, name="search_results")
]
