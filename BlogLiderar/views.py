from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, 'Base/inicio.html')

def sobre_nosotros(request):
    return render(request, 'Base/sobre_nosotros.html')