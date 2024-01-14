from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import html

from markdown2 import markdown

from . import util

class SubmitButton(forms.Input):
    input_type = "submit"
    def __init__(self, attrs=None):
        self.attrs = {"type":"submit"}


class SearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia")
    #plain HTML just works, it is fine
    attrs = {"type":"submit"}
    button = SubmitButton().render("s","Search", attrs={"type":"submit"})

class NewEntryForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea(attrs={"rows":"5"}))
    button = "<input type='submit' value='Search'></input>"


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            entry_name = form.cleaned_data["query"]

            if entry_name in util.list_entries():
                #I could't use reverse function here, because the website crashes if I use it
                return HttpResponseRedirect(f"/wiki/{entry_name}")
            else:
                if not util.search_results_for(entry_name):
                    return render(request, "encyclopedia/search_results.html",{
                        "messege":"Sorry, there is no entry matching your query"
                    })

                return render(request, "encyclopedia/search_results.html", {
                    "res" : util.search_results_for(entry_name)
                })
        else:
            return render(request, "encyclopedia/index.html", {
                "entries": util.list_entries(),
                "sform": SearchForm()
            })
    else:
        return render(request, "encyclopedia/index.html", {
            "entries": util.list_entries(),
            "sform": SearchForm()
        })


def entry(request, name):
    if md_content := util.get_entry(name):
        html_content = markdown(md_content)
    else:
        html_content = markdown("Sorry, no such entry was found")

    return render(request, "encyclopedia/entry.html",{
            "entry_content" : html_content,
            "entry_name" : name,
        })

def create_new_page(request):
    if request.method == "POST":
        form = forms.Form(request.POST)
    else:
        return render(request, "encyclopedia/new_page.html",{
            "neenform": NewEntryForm()
        })

