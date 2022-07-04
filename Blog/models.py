from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Categoria(models.Model):
    titulo= models.CharField(max_length=40)
    creado= models.DateTimeField(auto_now_add=True)
    actualizado= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'categoria'
        verbose_name_plural= 'categorias'

    def __str__(self):    
        return self.titulo

class Publicacion(models.Model):
    titulo= models.CharField(max_length=50)
    contenido= models.CharField(max_length=1000)
    autor=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to="blog", null=True, blank=True)
    creado= models.DateTimeField(auto_now_add=True)
    categorias= models.ManyToManyField(Categoria)
    actualizado= models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name= 'publicacion'
        verbose_name_plural= 'publicaciones'
    
    def __str__(self):    
        return self.titulo