from django.conf import settings
from django.db import models
from django.utils import timezone

EXPENSE_TYPES = [
    ('CT', 'Conta de Telefone'),
    ('CL', 'Conta de Luz'),
    ('CA', 'Conta de Água'),
    ('TX', 'Taxi'),
    ('VT', 'Veterinário'),
    ('RM', 'Remédios'),
    ('OT', 'Outros'),
]

class Expense(models.Model):
    expense_type = models.CharField(max_length=30, choices=EXPENSE_TYPES)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.description
