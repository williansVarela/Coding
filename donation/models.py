from django.conf import settings
from django.db import models
from django.utils import timezone

class Donation(models.Model):
    donation_type = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0) 
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.description
