from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import html

from markdown2 import markdown

from . import util


#this code for displaying a button is from here: https://djangosnippets.org/snippets/2312/
class SubmitButtonWidget(forms.Widget):
    def render(self, name, value, attrs=None, renderer=None):
        return '<input type="submit" name="%s" value="%s">' % (html.escape(name), html.escape(value))
class SubmitButtonField(forms.Field):
    def __init__(self, *args, **kwargs):
        kwargs["widget"] = SubmitButtonWidget
        super(SubmitButtonField, self).__init__(*args, **kwargs)
    def clean(self, value):
        return value



class SearchForm(forms.Form):
    query = forms.CharField(label="Search Encyclopedia")
    button = SubmitButtonField(initial=u"Search")


def index(request):
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            entry_name = form.cleaned_data["query"]

            if entry_name in util.list_entries():
                print("exists")
                return HttpResponseRedirect(f"/{entry_name}")
            else:
                print("doesn't exist")
                return HttpResponseRedirect(reverse("search_results"))
        else:
            print("invalid")
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

def search_results(request):
    res = util.search_results_for("")
    return render(request, "encyclopedia/search_results.html", {

    })
