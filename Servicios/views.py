from django.http import HttpResponse
from django.shortcuts import render
from Servicios.models import *

def servicios(request):
    return render(request, "Servicios/servicios.html")

