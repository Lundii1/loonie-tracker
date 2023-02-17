from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django import forms
from loonietracker.models import Expense, ExpenseForm
# Create your views here.
def home(request):
    expense_list = Expense.objects.all()
    total =  Expense.total()
    totalMonth = Expense.totalMonth()
    template = loader.get_template('loonietracker/home.html')
    context = {
        'expenses': expense_list,
        'total': total,
        'totalMonth':totalMonth,
    }
    return HttpResponse(template.render(context,request))
def expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    template = loader.get_template('loonietracker/expense.html')
    context = {
        'expense': expense,
    }
    return HttpResponse(template.render(context,request))
def expenseCreation(request):
    template = loader.get_template('loonietracker/expense_creation.html')
    context = {}
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
    else:
        form = ExpenseForm()
    return render(request, 'loonietracker/expense_creation.html', {'form': form})