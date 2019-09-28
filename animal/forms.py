from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Animal, Species, Breed, Shelter


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['name', 'sex', 'day_of_birth', 'species', 'breed', 'observation']
        labels = {
            'name': _('Nome'),
            'sex': _('Sexo'),
            'day_of_birth': _('Data de Nascimento'),
            'species': _('Espécie'),
            'breed': _('Raça'),
            'observation': _('Observação'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o nome do animal'}
        self.fields['sex'].widget.attrs = {'class': 'form-control'}
        self.fields['day_of_birth'].widget.attrs = {'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}
        self.fields['species'].widget.attrs = {'class': 'form-control'}
        self.fields['breed'].widget.attrs = {'class': 'form-control'}
        self.fields['observation'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite alguma observação'}


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

