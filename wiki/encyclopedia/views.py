from django.shortcuts import render
from markdown2 import markdown_path

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    html_content = markdown_path()
    return render()
