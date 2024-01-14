from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("edit_page", views.edit_page, name="edit_page"),
    path("new_page", views.create_new_page, name="new_page"),
    path("<str:name>", views.entry, name="entry"),
]
