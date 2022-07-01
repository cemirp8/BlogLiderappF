from distutils.command.clean import clean
from django.http import HttpResponse
from django.shortcuts import render
from Servicios.forms import *
from Servicios.models import *

def servicios(request):
    return render(request, "Servicios/servicios.html")

def newsletter_form(request):
    if request.method=="POST":
        newsletter_form= Newsletter_formulario(request.POST)

        if newsletter_form.is_valid():
            informacion= newsletter_form.cleaned_data
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            pais = request.POST['pais']
            newsletter = Newsletter(nombre=nombre, apellido=apellido, email=email, pais=pais)
            newsletter.save()
            mensaje = "Gracias por tu suscripción!"
            return render(request, "Servicios/newsletter_form.html", {'mensaje':mensaje,'newsletter_form':newsletter_form})

    else:
        newsletter_form= Newsletter_formulario()
    return render(request, "Servicios/newsletter_form.html", {'newsletter_form':newsletter_form})

def cursos_form(request):
    if request.method=="POST":
        cursos_form= Cursos_formulario(request.POST)

        if cursos_form.is_valid():
            informacion= cursos_form.cleaned_data
            nombre = request.POST['nombre']
            apellido = request.POST['apellido']
            email = request.POST['email']
            telefono = request.POST['telefono']
            curso = request.POST['curso']
            cursos = Cursos(nombre=nombre, apellido=apellido, email=email, telefono=telefono, curso=curso)
            cursos.save()
            mensaje = "Gracias por tu suscripción!"
            return render(request, "Servicios/cursos_form.html", {'mensaje':mensaje,'cursos_form':cursos_form})

    else:
        cursos_form= Cursos_formulario()
    return render(request, "Servicios/cursos_form.html", {'cursos_form':cursos_form})