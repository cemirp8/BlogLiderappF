from django.urls import path
from Servicios import views

urlpatterns = [
    path('servicios', views.servicios, name='servicios'),
    path('newsletter_form', views.newsletter_form, name='newsletter_form'),
    path('cursos_form', views.cursos_form, name='cursos_form'),
]
