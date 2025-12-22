from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def car_view(request):
    return HttpResponse ('Meus carros')
