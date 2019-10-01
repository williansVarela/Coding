from django.shortcuts import render
from django.utils import timezone
from .models import Expense

def expense_list(request):
    expenses = Expense.objects.all()

    context = {'pagina': 'Despesas', 'page_title': 'Despesas', 'expenses': expenses}
    return render(request, 'finance/expense_list.html', context)

