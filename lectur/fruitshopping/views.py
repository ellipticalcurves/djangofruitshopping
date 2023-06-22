from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "fruitshopping/index.html")

def greet(request, name):
    return render(request, "fruitshopping/base.html",
                  {
                      "name":name.capitalize()
                      }
                      )