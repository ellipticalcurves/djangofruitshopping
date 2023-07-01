from django.urls import path
from . import views


app_name = "shop"
urlpatterns = [
     path("", views.index, name="index"),
    #  path("<str:name>", views.greet, name="greet"),
     path("add", views.add, name="add")
 ]