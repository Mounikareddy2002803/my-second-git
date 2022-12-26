from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def first(request):
    return HttpResponse('first program in django')

def mouni(request):
    return HttpResponse('<h1> <marquee> MOUNIKA REDDY</marquee></h1>') 