from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Woo! We made a new route!')