from datetime import datetime
from django import forms
from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
class Expense(models.Model):
    amount = models.IntegerField(default=0)
    date = models.DateTimeField('date created',default=datetime.now)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    def __str__(self):
        return self
    def total():
        total = 0
        expenses = Expense.objects.filter()
        for expense in expenses:
           total+=expense.amount
        return total
    def totalMonth():
        total = 0
        now = datetime.now()
        expenses = Expense.objects.filter()
        for expense in expenses:
            if(expense.date.month == now.month and expense.date.year == now.year):
                total+=expense.amount
        return total

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['amount', 'date', 'category']