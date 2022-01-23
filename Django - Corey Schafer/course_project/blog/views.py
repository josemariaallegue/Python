from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
posts = [
    {"author": "natalia",
     "title": "blog post 1",
     "content": "1 post content",
     "datePosted": "27 august 2019"},
    {"author": "natalia2",
     "title": "blog post 2",
     "content": "2 post content",
     "datePosted": "27 august 2021"}]


def home(request):
    context = {"posts": posts}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
