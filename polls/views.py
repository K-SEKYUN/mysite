from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다\n집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 집가고싶다 ")

# Create your views here.
