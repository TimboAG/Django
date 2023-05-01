from django.shortcuts import render, HttpResponse
from .models import post


def index(request):
    miPost= post.objects.all()
    print(miPost)
    return render(request, "index.html", {"miPost": miPost})

def contenido(request, id):
    miPost= post.objects.get(id=id)
    return render(request, "contenido.html", {"miPost": miPost})
