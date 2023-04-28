from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def qabot(request):
    return HttpResponse("Hello World!")

def index(request):
    return render(request, 'qabot/index.html')