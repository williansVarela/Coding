from django.conf import settings
from django.db import models
from django.utils import timezone

class Expense(models.Model):
    expense_type = models.CharField(max_length=2)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=1)
    amount = models.DecimalField(max_digits=9, decimal_places=2, default=0) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.description
