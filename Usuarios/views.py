from django.shortcuts import redirect, render
from Usuarios.forms import *
from django.contrib.auth import authenticate, login
from django.contrib import messages


def registro_usuario(request):
    if request.method == "POST":
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data['username'], password= formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, "Te has registrado correctamente!")
            return redirect(to='inicio')
    return render(request, 'Registration/registro.html', {'form':CustomUserCreationForm})