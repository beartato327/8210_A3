from django import forms
from django.forms import ModelForm

from .models import Pet

class PetForm(ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_name','pet_age','pet_breed','pet_type']
        widgets = {
            'pet_age': forms.DateInput(attrs={'class':'datepicker'})
        }