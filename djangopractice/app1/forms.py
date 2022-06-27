from django import forms
from .models import InputModel
class Mform(forms.ModelForm):
    class Meta:
        model=InputModel
        fields='__all__'
