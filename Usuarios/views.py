from django.shortcuts import redirect, render
from Usuarios.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario= form.cleaned_data.get('username')
            clave= form.cleaned_data.get('password')
            user= authenticate(username=usuario, password=clave)
            if user is not None:
                login(request,user)
                mensaje = f'Bienvenido a LiderApp @{usuario}'
                return render(request, 'Base/inicio.html', {'mensaje':mensaje})
            else:
                mensaje = 'Usuario no encontrado. Te invitamos a registrarte!'
                return render(request, 'Registration/registro.html', {'mensaje':mensaje})
        else:   
            form = AuthenticationForm()
            mensaje = 'Usuario no encontrado. Te invitamos a registrarte!'
            return render(request, 'Registration/login.html', {'mensaje':mensaje, 'form':form})
    else:
        form = AuthenticationForm()
        return render (request, "Registration/login.html", {'form':form} )

def register_request(request):
    if request.method == "POST":
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            username = formulario.cleaned_data['username']
            formulario.save()
            clave = formulario.cleaned_data['password1']
            user= authenticate(username=username, password=clave)
            login(request,user)
            mensaje = f'Bienvenido @{username}'
            return render(request, "Base/inicio.html", {'mensaje':mensaje})
        else:
            formulario = CustomUserCreationForm
            mensaje = f'No fue posible crear el usuario!'
            return render(request, "Registration/registro.html", {'mensaje':mensaje, 'form':formulario})
    else:
        formulario = CustomUserCreationForm()
        return render(request, 'Registration/registro.html', {'form':formulario})