from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Todo

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Login'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password'}))
    class Meta:
        model = User
        fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Введите имя пользователя'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Подтвердите пароль'}))
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['title', 'description', 'img']