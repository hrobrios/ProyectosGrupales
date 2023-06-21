from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Entrenador

class JugadorForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    email = forms.EmailField()
    celular = forms.CharField(max_length=15)
    telefono = forms.CharField(max_length=15)
    equipo = forms.IntegerField()
    fecha_ingreso = forms.DateField()

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmacion contraseña", widget=forms.PasswordInput)
    date = forms.DateField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields}

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model=Entrenador
        fields="__all__"