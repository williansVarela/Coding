from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Expense
from .forms import ExpenseForm

def expense_list(request):
    expenses = Expense.objects.all()

    context = {'pagina': 'Despesas', 'page_title': 'Despesas', 'expenses': expenses}
    return render(request, 'finance/expense_list.html', context)


def expense_detail(request, pk):
    expense = get_object_or_404(Expense, pk=pk)
    context = {'pagina': 'Despesas', 'page_title': 'Despesas', 'expense': expense}
    return render(request, 'finance/expense_detail.html', context)

def expense_new(request):
    form = ExpenseForm(request.POST or None)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.created_at = timezone.now()
        expense.status = "A"
        expense.save()
        return redirect('expense_detail', pk=expense.pk)
    
    context = {'pagina': 'Despesas', 'page_title': 'Despesas', 'form': form}
    return render(request, 'finance/expense_edit.html', context)

def expense_edit(request, pk):
    expense = Expense.objects.get(pk=pk)
    form = ExpenseForm(request.POST or None, instance=expense)
    if form.is_valid():
        expense = form.save(commit=False)
        expense.updated_at = timezone.now()
        expense.save()
        return redirect('expense_detail', pk=expense.pk)

    context = {'pagina': 'Despesas', 'page_title': 'Despesas', 'form': form}
    return render(request, 'finance/expense_edit.html', context)

def expense_delete(request, pk):
    expense = Expense.objects.get(pk=pk)
    context = {'pagina': 'Despesas', 'page_title': 'Despesas'}
    Expense.objects.filter(pk=pk).delete()
    return redirect('expense_list')
