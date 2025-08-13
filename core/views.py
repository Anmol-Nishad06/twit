from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    """A simple view that returns a welcome message.
    return HttpResponse("Welcome to the backend core application!")"""
    return render(request, 'layout.html')