from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from django.conf import settings

# Create your views here.

def index(request):
    context = {"name":"zhang"}
    return render(request, "index.html", context)