from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from loonietracker.models import Expense
# Create your views here.
def home(request):
    return HttpResponse("Hello, Django!")
def expenses(request):
    expense_list = Expense.objects.filter()
    template = loader.get_template('loonietracker/expenses.html')
    context = {
        'expenses': expense_list,
    }
    return HttpResponse(template.render(context,request))
def expense(request, expense_id):
    expense = Expense.objects.get(pk=expense_id)
    template = loader.get_template('loonietracker/expense.html')
    context = {
        'expense': expense,
    }
    return HttpResponse(template.render(context,request))