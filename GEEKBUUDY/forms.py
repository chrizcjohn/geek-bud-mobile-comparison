from django import forms
from .models import *


class SpecForm(forms.ModelForm):
    class Meta:
        model = Spec
        fields = ['image']