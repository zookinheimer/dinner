from django import forms
from .models import dinner_list
from django.forms import ModelForm


class addreceipeform(ModelForm):
    class Meta:
        model = dinner_list
        fields = ['name', 'ingredients']