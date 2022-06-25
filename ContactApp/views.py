from django.http import HttpResponse
from django.shortcuts import render
from ContactApp.models import *
from ContactApp.forms import *

# Create your views here.

def dudaestudiante(request):
    if request.method == "POST":
        dudaFormulario= DudaEstudianteFormulario(request.POST)

        if dudaFormulario.is_valid():
            informacion= dudaFormulario.cleaned_data
            nombre= request.POST['nombre']
            apellido= request.POST['apellido']
            email= request.POST['email']
            mensaje= request.POST['mensaje']
            dudaestudiante= DudaEstudiante(nombre=nombre, apellido=apellido, email=email, mensaje=mensaje)
            dudaestudiante.save()
            return render(request, "ContactApp/duda_estudiante.html")
    else:
        dudaFormulario = DudaEstudianteFormulario()
    return render(request, 'ContactApp/duda_estudiante.html',{'dudaFormulario':dudaFormulario})

def interesado(request):
    if request.method == "POST":
        interesadoFormulario= interesadoFormulario(request.POST)

        if interesadoFormulario.is_valid():
            informacion= interesadoFormulario.cleaned_data
            nombre= request.POST['nombre']
            email= request.POST['email']
            telefono= request.POST['telefono']
            curso_de_interes= request.POST['curso_de_interes']
            interesado= Interesado(nombre=nombre, email=email, telefono=telefono, curso_de_interes=[curso_de_interes])
            interesado.save()
            return render(request, "ContactApp/interesado.html")
    else:
        interesadoFormulario = InteresadoFormulario()
    return render(request, 'ContactApp/interesado.html',{'interesadoFormulario':interesadoFormulario})

