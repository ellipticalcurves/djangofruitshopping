from django.http import HttpResponse
from django.shortcuts import render


items = ["apple", "banana", "watermelon"]

# Create your views here.
def index(request):

    return render(request,
                   "fruitshopping/index.html",
                   {"items":items} # variable name in htnl template | value
                   ) 


def add(request):
    return render(request, "fruitshopping/add.html")

def greet(request, name):
    return render(request,
                   "fruitshopping/base.html",
                  {
                      "name":name.capitalize()
                      }
                      )
