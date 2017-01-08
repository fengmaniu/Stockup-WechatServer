from django.shortcuts import render
from django.http import HttpResponse
from apps.personal.models import User_basic

def personal(request):
	a = User_basic.objects.get(user_name='czg')
	return HttpResponse("Hello, personal + "+a.user_stockcode)