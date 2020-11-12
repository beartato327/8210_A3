from django import forms

class PetForm(forms.Form):
    pet_type = forms.CharField()
    pet_name = forms.CharField()
    pet_breed = forms.CharField()
    pet_age = forms.IntegerField()