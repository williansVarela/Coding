from django import forms
from .models import Animal, Species, Breed, Shelter


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'sex', 'day_of_birth', 'species', 'breed', 'observation']


class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['name']


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['species', 'name']


class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['animal', 'category', 'date_entry', 'date_exit']
