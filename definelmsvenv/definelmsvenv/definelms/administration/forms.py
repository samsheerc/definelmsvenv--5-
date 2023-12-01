from django import forms
from django.forms import fields, widgets
from django.forms.models import ModelForm
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['designation']
        widgets = {
            'designation': forms.TextInput(attrs={'class':'form-control', 'id':'desigantionid'}),

        }
