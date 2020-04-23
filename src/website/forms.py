from django.forms import ModelForm

from django import forms
from .models import Rinvio

class RinvioModelForm(ModelForm):
    class Meta:
        model = Rinvio
        exclude = ('created',)