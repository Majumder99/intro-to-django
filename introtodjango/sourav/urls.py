from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home view"),
    path("profile/", views.profile, name="profile page")
]
