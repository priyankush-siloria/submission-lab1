# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home.models import UserProfile
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Username",
            "class": "form-control"
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "placeholder": "Email",
            "class": "form-control"
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password",
            "class": "form-control"
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "placeholder": "Password check",
            "class": "form-control"
        })
    )

    # Company Fields
    company_name = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "Company Name",
            "class": "form-control"
        })
    )
    company_description = forms.CharField(
        widget=forms.Textarea(attrs={
            "placeholder": "Company Description",
            "class": "form-control",
            "rows": 3
        }),
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',
                  'company_name', 'company_description')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_picture', 'default_language', 'company']
