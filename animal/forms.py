from django import forms
from .models import Animal, Species, Breed, Health, HealthLog, Shelter


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'sex', 'birthday', 'species', 'breed', 'observation']


class SpeciesForm(forms.ModelForm):
    class Meta:
        model = Species
        fields = ['name']


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['species', 'name']


class HealthLogForm(forms.ModelForm):
    class Meta:
        model = HealthLog
        fields = ['health', 'date', 'observation']


class HealthForm(forms.ModelForm):
    class Meta:
        model = Health
        fields = ['name']


class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['animal', 'category', 'entry_date', 'exit_date']
