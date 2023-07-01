from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

items = []#"apple", "banana", "watermelon"]

class NewItemForm(forms.Form):
    item = forms.CharField(label="New Item")
    # price = forms.IntegerField(label="price",
    #                             min_value=1,
    #                             max_value=5 )
# Create your views here.
def index(request):
    if "items" not in request.session:
        request.session["items"] = []
    return render(request,
                   "fruitshopping/index.html",
                   {"items":items} # variable name in htnl template | value
                   ) 


def add(request):
    if request.method=="POST":
        form = NewItemForm(request.POST)
        if form.is_valid():
            item = form.cleaned_data["item"]
            items.append(item)
            return HttpResponseRedirect(reverse("shop:index"))
        else:
            return render(request,
                        "fruitshopping/add.html",
                        {"form":form}
                        )

    return render(request,
                   "fruitshopping/add.html",
                   {
                       "form":NewItemForm()
                   }
                   
                   )

# def greet(request, name):
#     return render(request,
#                    "fruitshopping/base.html",
#                   {
#                       "name":name.capitalize()
#                       }
#                       )
