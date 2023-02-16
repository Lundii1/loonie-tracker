from datetime import datetime
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
