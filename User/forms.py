from django.forms import ModelForm
from django import forms
from django.contrib.auth import models

class UserSignup(ModelForm):
    password = forms.PasswordInput()
    class Meta:
        model = models.User
        fields = ['username','first_name','last_name','email']
    


class UserSigninUsername(forms.Form):
    
    username = forms.CharField()
    password = forms.PasswordInput()

class UserSigninEmail(forms.Form):
    email = forms.EmailField()
    password = forms.PasswordInput()

