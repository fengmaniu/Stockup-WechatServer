from django.shortcuts import render
from django.http import HttpResponse


def trend(request):
    return HttpResponse("Hello, trend")