from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import AnimalForm, SpeciesForm, BreedForm, ShelterForm, ShelterAnimalForm, ClinicalLogForm
from .models import Animal, Shelter, ClinicalLog


def animal(request):
    animals = []

    for animal_obj in Animal.objects.all():
        shelter_objs = Shelter.objects.filter(animal=animal_obj.id)
        if len(shelter_objs) > 0:
            shelter_category = shelter_objs.order_by('-date_entry')[0].category
            animal_obj.shelter_category = shelter_category
        else:
            animal_obj.shelter_category = None

        animal_obj.shelters = shelter_objs

        clinical_log_objs = ClinicalLog.objects.filter(animal=animal_obj.id).order_by('-date')
        animal_obj.clinical_log_objs = clinical_log_objs
        animals.append(animal_obj)

    context = {'pagina': 'Lista de Animais', 'page_title': 'Animais'}
    context['animals'] = animals
    return render(request, 'animal_list.html', context)


def new_animal(request):
    animal_form = AnimalForm(request.POST or None)
    shelter_form = ShelterAnimalForm(request.POST or None)

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
    animal_obj = Animal.objects.get(pk=pk)
    animal_obj.delete()
    return redirect('animal')


def new_species_popup(request):
    context = {}
    form = SpeciesForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_species");</script>' % (instance.pk, instance))

    context = {'pagina': 'Nova Espécie', 'page_title': 'Nova Espécie'}
    context['form'] = form
    return render(request, "ordinary_form.html", context)


def new_breed_popup(request):
    form = BreedForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_breed");</script>' % (instance.pk, instance))

    context = {'pagina': 'Nova Raça', 'page_title': 'Nova Raça'}
    context['form'] = form
    return render(request, "ordinary_form.html", context)


def new_clinical_log_popup(request, pk):
    clinical_log_form = ClinicalLogForm(request.POST or None)
#
    if clinical_log_form.is_valid():
        clinical_log_obj = clinical_log_form.save(False)
        clinical_log_obj.animal = Animal.objects.get(pk=pk)
        clinical_log_obj.save()

        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_clinical_log");</script>' % (clinical_log_obj.pk, clinical_log_obj))
#
    context = {'pagina': f'Nova Informação Clínica para {Animal.objects.get(pk=pk).name}', 'page_title': 'Nova Informação Clínica'}
    context['form'] = clinical_log_form
    return render(request, "ordinary_form.html", context)


def del_clinical_log(request, pk):
    clinical_log_obj = ClinicalLog.objects.get(pk=pk)
    clinical_log_obj.delete()
    return redirect('animal')


def shelter(request):
    context = {'pagina': 'Lista de Acolhimentos', 'page_title': 'Acolhimentos'}
    context['shelter'] = Shelter.objects.all()
    return render(request, 'shelter_list.html', context)


def new_shelter(request):
    form = ShelterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('shelter')

    context = {'pagina': 'Novo Acolhimento', 'page_title': 'Novo Acolhimento'}
    context['form'] = form
    return render(request, 'shelter_form.html', context)


def update_shelter(request, pk):
    shelter_obj = Shelter.objects.get(pk=pk)
    form = ShelterForm(request.POST or None, instance=shelter_obj)

    if form.is_valid():
        form.save()
        return redirect('shelter')

    context = {'pagina': 'Editar Acolhimento', 'page_title': 'Editar Acolhimento'}
    context['form'] = form
    context['shelter'] = shelter_obj
    return render(request, 'shelter_form.html', context)


def del_shelter(request, pk):
    shelter_obj = Shelter.objects.get(pk=pk)
    shelter_obj.delete()
    return redirect('shelter')


