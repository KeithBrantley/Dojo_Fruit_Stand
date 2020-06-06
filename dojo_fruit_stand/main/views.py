from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('This is actually fun!')

def checkout(request):
    return HttpResponse('This is the checkout page')