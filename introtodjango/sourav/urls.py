# we just declare all the urls in urls.py

from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home view"),
    path("profile/", views.profile, name="profile page"),
    path("article/<int:pk>/", views.singlearticle, name="article")
]
