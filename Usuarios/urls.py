from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', views.login_request, name='login_request'),
    path('register_request/', views.register_request, name='register_request'),
    path('logout/', LogoutView.as_view(template_name='Registration/logout.html'), name='logout')
]