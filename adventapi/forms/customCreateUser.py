from django import forms
from django.contrib.auth.forms import BaseUserCreationForm, UsernameField
from adventapi.models import CustomUser

class CustomCreateUserForm(forms.Form, BaseUserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username",)
        field_classes = {"username": UsernameField}
