from django.shortcuts import redirect, render
from Usuarios.forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


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

@login_required
def edicion_usuario(request):
    usuario = request.user
    if request.method == "POST":
        formulario = UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.first_name= informacion['first_name']
            usuario.last_name= informacion['last_name']
            usuario.email= informacion['email']
            usuario.password1= informacion['password1']
            usuario.password2= informacion['password2']
            usuario.save()
            mensaje = 'Cambios guardados exitosamente!'
            return render(request, "Base/inicio.html", {'mensaje':mensaje, 'usuario':usuario})
    else:
        formulario = UserEditForm(instance=usuario)
    return render(request, "Registration/edicion_usuario.html", {'form':formulario, 'usuario':usuario.username})

@login_required
def eliminacion_usuario(request, username):
        usuario= User.objects.get(username=username)
        usuario.delete()
        mensaje = 'Usuario borrado exitosamente. Esperamos volverte a ver pronto!'
        logout(request)
        return render(request, "Base/inicio.html", {'mensaje':mensaje})