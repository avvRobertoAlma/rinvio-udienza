from django.forms import ModelForm

from django import forms
from .models import Rinvio, Giudice

class RinvioModelForm(ModelForm):
    class Meta:
        model = Rinvio
        exclude = ('created',)

class RinvioGiudiceModelForm(ModelForm):
    class Meta:
        model = Rinvio
        exclude = ('ufficio', 'giudice', 'created')