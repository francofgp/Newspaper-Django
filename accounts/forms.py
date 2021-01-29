from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        # para la contraseña no se especifica porque es requerido
        #fields = UserCreationForm.Meta.fields + ('age',)
        # para agregar el campo de email, que ya trae por defecto, usamos
        fields = ('username', 'email', 'age',)
        # le especificamos todos los campos que queremos


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',)
