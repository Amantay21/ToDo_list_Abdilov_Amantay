from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MyUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email address")

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                  'first_name', 'last_name', 'email']
        field_classes = {'username': UsernameField}

    def clean(self):
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if not (first_name or last_name):
            raise forms.ValidationError("хотя бы одно из полей first_name или last_name должно быть заполненным")
        elif password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return cleaned_data

