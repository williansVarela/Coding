from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AnimalForm, SpeciesForm, BreedForm, HealthLogForm, HealthForm, ShelterForm
from .models import Animal, Shelter


def animal(request):
    animals = []

    for animal_obj in Animal.objects.all():
        shelter_objs = Shelter.objects.filter(animal = animal_obj.id)
        if len(shelter_objs) > 0:
            category = shelter_objs.order_by('-entry_date')[0].category
            animal_obj.category = category
        else:
            animal_obj.category = None
        animals.append(animal_obj)

    context = {'pagina': 'Lista de Animais', 'page_title': 'Animais'}
    context['animals'] = animals
    return render(request, 'animal_list.html', context)


def new_animal(request):
    data = {}
    animal_form = AnimalForm(request.POST or None)
    healthlog_form = HealthLogForm(request.POST or None)

    if animal_form.is_valid():
        animal_obj = animal_form.save()
        if healthlog_form.is_valid():
            healthlog_obj = healthlog_form.save(False)
            healthlog_obj.animal = animal_obj
            healthlog_obj.save()
        return redirect('animal')

    data['action'] = 'create'
    data['animal_form'] = animal_form
    data['healthlog_form'] = healthlog_form
    return render(request, 'animal_form.html', data)


def update_animal(request, pk):
    data = {}
    animal_obj = Animal.objects.get(pk=pk)
    form = AnimalForm(request.POST or None, instance=animal_obj)

    if form.is_valid():
        form.save()
        return redirect('animal')

    data['action'] = 'update'
    data['animal_form'] = form
    data['animal'] = animal_obj
    return render(request, 'animal_form.html', data)


def del_animal(request, pk):
    animal_obj = Animal.objects.get(pk=pk)
    animal_obj.delete()
    return redirect('animal')


def new_species_popup(request):
    data = {}
    form = SpeciesForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_species");</script>' % (instance.pk, instance))

    data['form'] = form
    return render(request, "species_form.html", data)


def new_breed_popup(request):
    data = {}
    form = BreedForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_breed");</script>' % (instance.pk, instance))

    data['form'] = form
    return render(request, "breed_form.html", data)


def new_health_popup(request):
    data = {}
    form = HealthForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_health");</script>' % (instance.pk, instance))

    data['form'] = form
    return render(request, "health_form.html", data)


def shelter(request):
    data = {}
    data['shelter'] = Shelter.objects.all()
    return render(request, 'shelter_list.html', data)


def new_shelter(request):
    data = {}
    form = ShelterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('shelter')

    data['form'] = form
    return render(request, 'shelter_form.html', data)


def update_shelter(request, pk):
    data = {}
    shelter_obj = Shelter.objects.get(pk=pk)
    form = ShelterForm(request.POST or None, instance=shelter_obj)

    if form.is_valid():
        form.save()
        return redirect('shelter')

    data['form'] = form
    data['shelter'] = shelter_obj
    return render(request, 'shelter_form.html', data)


def del_shelter(request, pk):
    shelter_obj = Shelter.objects.get(pk=pk)
    shelter_obj.delete()
    return redirect('shelter')
