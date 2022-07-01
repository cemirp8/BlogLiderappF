from django.contrib import admin
from .models import *

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')

class PublicacionAdmin(admin.ModelAdmin):
    readonly_fields=('creado', 'actualizado')

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacion, PublicacionAdmin)