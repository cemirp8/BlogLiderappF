from django.shortcuts import render
from Blog.forms import *
from Blog.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

def blog(request):
    publicaciones=Publicacion.objects.all
    return render(request, "Blog/blog.html", {"publicaciones": publicaciones})

def categoria(request, categoria_id):
    categoria=Categoria.objects.get(id=categoria_id)
    publicaciones=Publicacion.objects.filter(categorias=categoria)
    return render(request, "blog/categoria.html", {'categoria':categoria, 'publicaciones':publicaciones})

def buscar(request):
    if request.GET['contenido']:
        contenido = request.GET['contenido']
        publicaciones = Publicacion.objects.filter(contenido__icontains=contenido)
        if len(publicaciones) == 0:
            publicaciones=Publicacion.objects.all
            mensaje = "No existen coincidencias"
            return render(request, "Blog/blog.html", {"publicaciones": publicaciones, "mensaje":mensaje})
        return render(request, "Blog/buscarContenido.html", {"publicaciones":publicaciones})
    else:
        publicaciones=Publicacion.objects.all
        mensaje = "Ingrese una búsqueda válida"    
        return render(request, "Blog/blog.html", {"publicaciones": publicaciones, "mensaje":mensaje})

@login_required
def publicaciones(request):
    if request.method == 'POST':
        formulario = Publicacion_Form(request.POST)
        
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            titulo = request.POST['titulo']
            contenido = request.POST['contenido']
            usuario= request.user
            autor=User.objects.get(username=usuario.username)
            publicacion=Publicacion(titulo=titulo, contenido=contenido, autor=autor)
            publicacion.save()
            mensaje = "Publicacion creada. Gracias por tu contribución!"

            return render(request, "Base/inicio.html", {"mensaje":mensaje})
    else: 
            formulario=Publicacion_Form()

    return render(request, "Blog/crearBlog.html", {"formulario":formulario})


