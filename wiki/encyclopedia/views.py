from django.shortcuts import render
from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    try:
        with open(f"entries/{name}.md") as file:
            md_content = file.read()
    except FileNotFoundError:
        md_content = "There is no such entry"

    html_content = markdown(md_content)
    return render(request, "encyclopedia/entry.html",{
        "entry_content" : html_content,
        "entry_name" : name
    })