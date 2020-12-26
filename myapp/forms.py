from django.forms import ModelForm
#auth form
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms
from .models import *

class blogForm(ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        

        widgets = {            
            'author': forms.TextInput(attrs={'class':'form-control d-none'}),
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            'body_text': forms.Textarea(attrs={'class':'form-control'}),
            'tag': forms.CheckboxSelectMultiple(attrs={'class':'form-check'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Password'}),
            'password2': forms.PasswordInput(attrs={'class':'form-control','placeholder':'Re-type password'}),
        }