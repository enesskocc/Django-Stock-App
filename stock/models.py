from django.db import models
from django.contrib.auth.models import User

status_choices = [
    ('I', 'IN'),
    ('O', 'OUT'),
]

class Firm(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    adress = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) ## category silinirse, yerine null ata(set_null)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    stockk = models.IntegerField()

    def __str__(self):
        return f"{self.name}" 


class Stock(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    firm = models.ForeignKey(Firm,  on_delete=models.SET_NULL, null=True)
    transaction = models.CharField(max_length=1, choices= status_choices)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantitiy = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True)

    def __str__(self):
         return f'{self.transaction} - {self.product} - {self.quantitiy}'  




