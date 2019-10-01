from django.conf import settings
from django.db import models
from django.utils import timezone

DONATION_TYPES = [
    ('DN', 'Dinheiro'),
    ('DC', 'Depósito em Conta'),
    ('TR', 'Transferência'),
    ('OT', 'Outros'),
]

class Donation(models.Model):
    donation_type = models.CharField(max_length=30, choices=DONATION_TYPES)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.description
