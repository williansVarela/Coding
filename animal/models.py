from django.db import models


class Species(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name="Espécie")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        self.name = self.name.title()
        super(Species, self).save(force_insert, force_update)


class Breed(models.Model):
    name = models.CharField(max_length=30, verbose_name="Raça")
    species = models.ForeignKey(Species, on_delete=models.CASCADE, verbose_name="Espécie")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        self.name = self.name.title()
        super(Breed, self).save(force_insert, force_update)


class Animal(models.Model):
    SEX_CHOICES = [
        ('F', 'Fêmea'),
        ('M', 'Macho')
    ]
    name = models.CharField(max_length=30, verbose_name="Nome")
    sex = models.CharField(max_length=1, choices=SEX_CHOICES, default="F", verbose_name="Sexo")
    day_of_birth = models.DateField(verbose_name="Data Nascimento")
    species = models.ForeignKey(Species, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Espécie")
    breed = models.ForeignKey(Breed, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Raça")
    observation = models.CharField(max_length=140, null=True, blank=True, verbose_name="Observação")

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False):
        self.name = self.name.title()
        super(Animal, self).save(force_insert, force_update)


class ClinicalLog(models.Model):
    clinical_condition = models.CharField(max_length=55, verbose_name="Estado Clínico")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    date = models.DateField(verbose_name="Data")

    def __str__(self):
        return self.clinical_condition


class Shelter(models.Model):
    SHELTER_CHOICES = [
        ('Temporário', 'Temporário'),
        ('Adoção', 'Adoção')
    ]

    person = models.ForeignKey('contacts.Contact', on_delete=models.PROTECT, verbose_name="Pessoa")
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, verbose_name="Animal")
    category = models.CharField(max_length=10, choices=SHELTER_CHOICES, verbose_name="Categoria")
    date_entry = models.DateField(verbose_name="Data Entrada")
    date_exit = models.DateField(null=True, blank=True, verbose_name="Data Saída")

    def __str__(self):
        return self.person.person.name + " <- " + self.animal.name + " - " + str(self.date_entry)
