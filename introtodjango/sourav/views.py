from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    # return HttpResponse("hello world")
    return render(request, "sourav/index.html")


def profile(request):
    return render(request, "sourav/profile.html")
