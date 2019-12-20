from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, "shop/index.html")


def product(request):
    return HttpResponse("Products Page")


def about(request):
    return HttpResponse("About Us page")


def contact(request):
    return HttpResponse("Contact Page")


def cart(request):
    return HttpResponse("Cart Page")


def pland(request):
    return HttpResponse("Single Product Page")
