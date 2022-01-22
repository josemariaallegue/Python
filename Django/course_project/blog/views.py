from django.shortcuts import render
from django.http import HttpResponse, response

# Create your views here.


def home(request):
    return HttpResponse("<h1>Blog Home</h1>")


def about(request):
    texto = ""

    for i in range(1, 10):
        texto += f"numero: {str(i)}\n\n"

    return HttpResponse(f"<h2>{texto}</h2>")
