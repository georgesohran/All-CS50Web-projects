from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from markdown2 import markdown

from . import util


def index(request):
    if request.method == "POST":
        form = forms.Form(request.POST)
        print(form)
        if form.is_valid():
            entry_name = form.cleaned_data["q"]

            if entry_name in util.list_entries():
                return HttpResponseRedirect(reverse(f"{entry_name}"))
            else:
                ...
                return render(request, "encyclopedia/search_results.html")
        else:
            print("invalid form")
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries()
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries()
        })


def entry(request, name):
    if md_content := util.get_entry(name):
        html_content = markdown(md_content)
        return render(request, "encyclopedia/entry.html",{
            "entry_content" : html_content,
            "entry_name" : name
        })

    html_content = markdown("Sorry, no such entry was found")
    return render(request, "encyclopedia/entry.html",{
            "entry_content" : html_content,
            "entry_name" : name
        })

def search_results(request):
    return render(request, "encyclopedia/search_results.html")
