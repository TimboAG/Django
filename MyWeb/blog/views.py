from django.shortcuts import render, HttpResponse


def index(request):
    return HttpResponse("Hola mundo con Django")
