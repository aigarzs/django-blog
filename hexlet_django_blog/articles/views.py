from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context = {"appname": "Simple Django Blog"}
	return render(request, "articles/index.html", context=context)
