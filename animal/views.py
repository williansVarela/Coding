from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnimalForm, SpeciesForm, BreedForm, ShelterForm, ClinicalLogForm
from .models import Animal, Shelter, ClinicalLog


def animal(request):
    animals = []

    for animal_obj in Animal.objects.all():
        shelter_objs = Shelter.objects.filter(animal=animal_obj.id).order_by('-date_entry')
        if len(shelter_objs) > 0:
            shelter_category = shelter_objs[0].category
            animal_obj.shelter_category = shelter_category
        else:
            animal_obj.shelter_category = None

        animal_obj.shelters = shelter_objs

        clinical_log_objs = ClinicalLog.objects.filter(animal=animal_obj.id).order_by('-date')
        animal_obj.clinical_logs = clinical_log_objs
        animals.append(animal_obj)

    context = {'pagina': 'Lista de Animais', 'page_title': 'Animais'}
    context['animals'] = animals
    return render(request, 'animal_list.html', context)


def new_animal(request):
    animal_form = AnimalForm(request.POST or None)
    shelter_form = ShelterForm(request.POST or None)

    if animal_form.is_valid():
        animal_obj = animal_form.save()
        if shelter_form.is_valid():
            shelter_obj = shelter_form.save(False)
            shelter_obj.animal = animal_obj
            shelter_obj.save()
        return redirect('animal')

    context = {'pagina': 'Novo Animal', 'page_title': 'Novo Animal'}
    context['animal_form'] = animal_form
    context['shelter_form'] = shelter_form
    context['is_creation'] = True
    return render(request, 'animal_form.html', context)


def update_animal(request, pk):
    animal_obj = Animal.objects.get(pk=pk)
    form = AnimalForm(request.POST or None, instance=animal_obj)

    if form.is_valid():
        form.save()
        return redirect('animal')

    context = {'pagina': 'Editar Animal', 'page_title': 'Editar Animal'}
    context['action'] = 'update'
    context['animal_form'] = form
    context['animal'] = animal_obj
    return render(request, 'animal_form.html', context)


def del_animal(request, pk):
    animal = Animal.objects.get(pk=pk)
    animal.delete()
    return redirect('animal')


def new_species_popup(request):
    form = SpeciesForm(request.POST or None)

    if form.is_valid():
        species = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_species");</script>' % (species.pk, species))

    context = {'pagina': 'Nova Espécie', 'page_title': 'Nova Espécie'}
    context['form'] = form
    return render(request, "ordinary_form.html", context)


def new_breed_popup(request):
    form = BreedForm(request.POST or None)

    if form.is_valid():
        breed = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_breed");</script>' % (breed.pk, breed))

    context = {'pagina': 'Nova Raça', 'page_title': 'Nova Raça'}
    context['form'] = form
    return render(request, "ordinary_form.html", context)


def new_clinical_log(request, pk):
    form = ClinicalLogForm(request.POST or None)

    if form.is_valid():
        clinical_log = form.save(False)
        clinical_log.animal = Animal.objects.get(pk=pk)
        clinical_log.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_clinical_log");</script>' % (clinical_log.pk, clinical_log))

    context = {'pagina': 'Nova Informação Clínica', 'page_title': 'Nova Informação Clínica'}
    context['form'] = form
    return render(request, "ordinary_form.html", context)


def update_clinical_log(request, pk):
    clinical_log = ClinicalLog.objects.get(pk=pk)
    form = ClinicalLogForm(request.POST or None, instance=clinical_log)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_clinical_log");</script>' % (clinical_log.pk, clinical_log))

    context = {'pagina': 'Editar Informação Clínica', 'page_title': 'Editar Informação Clínica'}
    context['form'] = form
    context['clinical_log'] = clinical_log
    return render(request, 'ordinary_form.html', context)


def del_clinical_log(request, pk):
    clinical_log_obj = ClinicalLog.objects.get(pk=pk)
    clinical_log_obj.delete()
    return redirect('animal')



def new_shelter(request, pk):
    form = ShelterForm(request.POST or None)

    if form.is_valid():
        shelter = form.save(False)
        shelter.animal = Animal.objects.get(pk=pk)
        shelter.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_shelter");</script>' % (shelter.pk, shelter))

    context = {'pagina': 'Novo Acolhimento', 'page_title': 'Novo Acolhimento'}
    context['form'] = form
    return render(request, 'ordinary_form.html', context)


def update_shelter(request, pk):
    shelter = Shelter.objects.get(pk=pk)
    form = ShelterForm(request.POST or None, instance=shelter)

    if form.is_valid():
        form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_shelter");</script>' % (shelter.pk, shelter))

    context = {'pagina': 'Editar Acolhimento', 'page_title': 'Editar Acolhimento'}
    context['form'] = form
    context['shelter'] = shelter
    return render(request, 'ordinary_form.html', context)


def del_shelter(request, pk):
    shelter = Shelter.objects.get(pk=pk)
    shelter.delete()
    return redirect('animal')
