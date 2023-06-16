from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.welcome, name='home'),
    path('users/', views.home, name="users"), #endpoint
    path('clients/', views.view_client, name="clients"),
    path('jugador_formulario/', views.crear_jugador, name='jugador_formulario'),
    # path('register_user', views.register_user, name="register_user"),
    path('register_user/', views.register_user, name='register_user'),
]
