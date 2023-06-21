from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .forms import JugadorForm, EntrenadorForm
from .models import Jugador, Entrenador
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm
# Create your views here.

def welcome(request):
    return render(request, "home.html")

def home(request):
    users = User.objects.all()

    nuevos = ["", ""]

    context = {
        "usuarios": users,
        "otros": nuevos,
    }

    return render(request, "users.html", context=context)

@login_required
def view_client(request):

    context = {"nombre": "Club Barcelona",
                "edad":200,
                "oficio":"Club de Futbol Profesional"}
    
                   
    return render(request, 'clients.html', context=context)

def crear_jugador(request):
    form = JugadorForm()

    if request.method == "POST":
        print(request)
        form = JugadorForm(request.POST)

        if form.is_valid():
                print (form)
                jugador = Jugador()
                jugador.nombre = form.cleaned_data['nombre']
                jugador.apellido = form.cleaned_data['apellido']
                jugador.edad = form.cleaned_data['edad']
                jugador.email = form.cleaned_data['email']
                jugador.celular = form.cleaned_data['celular']
                jugador.telefono = form.cleaned_data['telefono']
                jugador.egreso = form.cleaned_data['egreso']
                jugador.fecha_contratacion = form.cleaned_data['fecha_contratacion']
                jugador.save()
        else:
            print("Datos invalidos")
        return redirect('/home')
    
    context = {
        'form': form
    }

    return render(request, 'jugador_formulario.html', context=context)

# def register_user(request):
#     user = User.objects.create(
#         username="RodrigoF",
#         password="1234rodrigo",
#         is_staff=True
#     )
#     user.save()
#     return redirect('/home')

def register_user(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente!!')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    
    context = {'form': form}
    return render(request, 'register_user.html', context)

def signout(request):
    logout(request)
    return redirect('home')

def login_page(request):
    if request.method == 'GET':
        return render(request, 'login_page.html',{
        'form':AuthenticationForm
        })
    else:
        user = authenticate(request, username= request.POST['username'], password= request.POST['password'])
        if user is None:
            return render(request, 'login_page.html',{
            'form':AuthenticationForm,
            'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('home')

def Entrenador(request):
    form=EntrenadorForm()

    if request.method =="POST":
        form = EntrenadorForm(request.POST)
        if form.is_valid():
            print(form)
            entrenador= Entrenador()
            entrenador.nombre=form.cleaned_data["nombre"]
            entrenador.apellido=form.cleaned_data["apellido"]
            entrenador.email=form.cleaned_data["email"]
            entrenador.save()
        else:
            print("datos invalidos")
        return redirect("/home")
    context ={"form":form}

    return render(request, "formulario.html", context=context)