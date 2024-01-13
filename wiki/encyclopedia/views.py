from django.shortcuts import render
from django import forms
from markdown2 import markdown

from . import util


def index(request):
    if request.method == "POST":
        print(forms.Form(request.POST))


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
