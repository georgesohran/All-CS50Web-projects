from django.shortcuts import render
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    with open("entries/CSS.md") as file:
        md_content = file.read()
    html_content = markdown(md_content)
    return render()
