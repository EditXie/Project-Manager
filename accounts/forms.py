from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserAdminCreationForm(UserCreationForm):
    ''' Cadastro de User '''
    username = forms.CharField(label='Nome do usuário')
    first_name = forms.CharField(label='Primeiro nome')
    last_name = forms.CharField(label='Sobrenome')
    email = forms.CharField(label='E-mail')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
