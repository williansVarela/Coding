from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome da Espécie")

    def __str__(self):
        return self.name


class Breed(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome da Raça")
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Espécie")

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=30, verbose_name="Nome")
    age = models.IntegerField(null=True, blank=True, verbose_name="Idade")
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Espécie")
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Raça")
    observation = models.CharField(max_length=140, null=True, blank=True, verbose_name="Observação")

    def __str__(self):
        return self.name


class Health(models.Model):
    name = models.CharField(max_length=30, verbose_name="Status de Saúde")

    def __str__(self):
        return self.name


class HealthLog(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    health = models.ForeignKey(Health, on_delete=models.CASCADE, verbose_name="Status de Saúde")
    date = models.DateField(verbose_name="Data")
    observation = models.CharField(max_length=140, null=True, blank=True, verbose_name="Observação")

    def __str__(self):
        return self.animal.name + " - " + self.health.name


class Shelter(models.Model):
    person = None
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    is_temporary = models.BooleanField(verbose_name="Abrigo Temporário")
    entry_date = models.DateField(verbose_name="Data de Entrada")
    exit_date = models.DateField(null=True, blank=True, verbose_name="Data de Saída")

    def __str__(self):
        return self.animal.name + " - " + str(self.entry_date)
