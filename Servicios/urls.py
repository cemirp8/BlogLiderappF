from django.urls import path
from Servicios import views

urlpatterns = [
    path('servicios', views.servicios, name='servicios'),
]
