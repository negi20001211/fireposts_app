from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    group = forms.ModelChoiceField(queryset=Group.objects.all(), label='所属')