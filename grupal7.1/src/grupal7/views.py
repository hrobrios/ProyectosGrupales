from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm, PedidoForm
from .models import Pedido, Historial


def home(request):
    return render(request, "home.html")

@login_required
def registro_usuario(request):#el request es todo lo que traemos desde hmtl
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)#se crea instancia userregistration
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            permissions = form.cleaned_data['permissions']
            username = form.cleaned_data['username']
            user.groups.add(group)
            user.user_permissions.set(permissions)
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('/home')
    else: 
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'registro_usuario.html', context)


def login(request):
        if request.method=="POST":
            form = LoginForm (request.POST)
            if form.is_valid():
                usuario = form.cleaned_data["nombre"]
                clave = form.cleaned_data["password"]
                user = authenticate(request, username=usuario, password=clave)
                if user is not None:
                        if user.is_active:
                            auth_login(request, user)
                            return redirect('/home')
                else:
                    return HttpResponse('Cuenta deshabilitada')
            else:
                return HttpResponse('Login no valido')
        else:
            form = LoginForm()
        return render(request, 'aplicacion/login.html', {'form':form})

def logout(request):
        auth_logout(request)
        return redirect('/login')


@login_required
def formulario(request):
    form = PedidoForm()

    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            print(form)
            pedido = Pedido()
            pedido.nombre = form.cleaned_data['nombre']
            pedido.direccion = form.cleaned_data['direccion']
            pedido.email = form.cleaned_data['email']
            pedido.save()
        else:
            print("Datos invalidos")
        return redirect('/mostrar_escuela')
    context = {'form': form}

    return render(request, 'pedidos.html', context=context)


@login_required
def historial(request):

    datos = Historial.objects.all()

    context = {'historial': datos}

    return render(request, 'historial.html', context=context)