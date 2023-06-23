from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm
from .forms import JugadorForm
from .models import Jugador
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType


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

#######   funciones para generar el admin de usuarios 
def admin_usuarios(request):
    if request.method == 'POST':
        if 'create_user' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            group_id = request.POST['group']

            user = User.objects.create_user(username=username, password=password)
            group = Group.objects.get(id=group_id)
            user.groups.add(group)

        elif 'update_user' in request.POST:
            user_id = request.POST['user_id']
            username = request.POST['username']
            password = request.POST['password']
            group_id = request.POST['group']

            user = User.objects.get(id=user_id)
            user.username = username
            if password:
                user.set_password(password)
            user.groups.clear()
            group = Group.objects.get(id=group_id)
            user.groups.add(group)
            user.save()

        elif 'delete_user' in request.POST:
            user_id = request.POST['user_id']
            user = User.objects.get(id=user_id)
            user.delete()

        elif 'create_group' in request.POST:
            name = request.POST['group_name']
            group = Group.objects.create(name=name)

        elif 'update_group' in request.POST:
            group_id = request.POST['group_id']
            name = request.POST['group_name']

            group = Group.objects.get(id=group_id)
            group.name = name
            group.save()

        elif 'delete_group' in request.POST:
            group_id = request.POST['group_id']
            group = Group.objects.get(id=group_id)
            group.delete()

        elif 'create_permission' in request.POST:
            name = request.POST['permission_name']
            
           
            
        elif 'update_permission' in request.POST:
            permission_id = request.POST['permission_id']
            name = request.POST['permission_name']
            content_type_id = request.POST['content_type']
            

            permission = Permission.objects.get(id=permission_id)
            permission.name = name
            permission.content_type = ContentType.objects.get(id=content_type_id)
            
            permission.save()

        elif 'delete_permission' in request.POST:
            permission_id = request.POST['permission_id']
            permission = Permission.objects.get(id=permission_id)
            permission.delete()

        return redirect('admin_usuarios')

    users = User.objects.all()
    groups = Group.objects.all()
    permissions = Permission.objects.all()
    content_types = ContentType.objects.all()

    return render(request, 'admin_usuarios.html', {
        'users': users,
        'groups': groups,
        'permissions': permissions,
        
    })