from django.shortcuts import render
from django.http import HttpRequest
# Create your views here.

def inicio(request):
    return HttpRequest("Sitio de venta"),