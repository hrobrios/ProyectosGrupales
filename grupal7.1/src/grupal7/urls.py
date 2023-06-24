from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('registro_usuario/', views.registro_usuario, name='registro_usuario'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('pedidos/', views.Pedido, name='pedidos.html'),
    path('historial/', views.Historial, name='historial.html'),

    #path('clients/', views.view_client, name="clients"),
    #path('formulario_profesor/', views.crear_profesor, name='formulario_profesor'),
    # path('register_user', views.register_user, name="register_user"),
    #path('users/', views.home, name="users"),
    #
    
]
