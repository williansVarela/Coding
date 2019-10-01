from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Animal, Species, Breed, Shelter, ClinicalLog


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
        labels = {'name': _('Espécie'),}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o nome da nova espécie'}


class BreedForm(forms.ModelForm):
    class Meta:
        model = Breed
        fields = ['species', 'name']
        labels = {
            'species': _('Espécie'),
            'name': _('Raça'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['species'].widget.attrs = {'class': 'form-control'}
        self.fields['name'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite o nome da nova raça'}


class ShelterForm(forms.ModelForm):
    class Meta:
        model = Shelter
        fields = ['category', 'person', 'date_entry', 'date_exit']
        labels = {
            'category': _('Tipo de Acolhimento'),
            'person': _('Acolhedor'),
            'date_entry': _('Data de Entrada'),
            'date_exit': _('Data de Saída'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['category'].widget.attrs = {'class': 'form-control'}
        self.fields['person'].widget.attrs = {'class': 'form-control'}
        self.fields['date_entry'].widget.attrs = {'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}
        self.fields['date_exit'].widget.attrs = {'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}


class ClinicalLogForm(forms.ModelForm):
    class Meta:
        model = ClinicalLog
        fields = ['clinical_condition', 'date']
        labels = {
            'clinical_condition': _('Informação Clínica'),
            'date': _('Data'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['clinical_condition'].widget.attrs = {'class': 'form-control', 'placeholder': 'Digite a informação clínica'}
        self.fields['date'].widget.attrs = {'class': 'form-control', 'placeholder': 'DD/MM/AAAA'}

