from logging import exception
from django.http import HttpResponse
from django.shortcuts import render

def inicio(request):
    return render(request, 'Base/inicio.html')

def sobre_nosotros(request):
    return render(request, 'Base/sobre_nosotros.html')

def error_404(request, exception):
    data = {}
    return render(request, 'Mensajes/error.html', data)

def error_500(request):
    data = {}
    return render(request, 'Mensajes/error.html', data)