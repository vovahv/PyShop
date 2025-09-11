from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Index.")

def new(request):
    return HttpResponse("New Products")