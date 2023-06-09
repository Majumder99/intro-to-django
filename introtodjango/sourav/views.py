# we just declare all the views meaning templates in views.py

from django.shortcuts import render
from django.http import HttpResponse
from . models import Article
# Create your views here.


def home(request):
    # return HttpResponse("hello world")
    # we are writing query here to get the data from the models
    articles = Article.objects.all()
    context = {'articles': articles}
    return render(request, "sourav/index.html", context=context)


def profile(request):
    return render(request, "sourav/profile.html")


def singlearticle(request, pk):
    article = Article.objects.get(id=pk)
    context = {"article": article}
    return render(request, 'sourav/singlearticle.html', context=context)
