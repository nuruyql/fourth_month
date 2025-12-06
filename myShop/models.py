from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.TextField(verbose_name='choose category')

    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(verbose_name='enter name')
    price = models.DecimalField(max_digits=10,decimal_places=2 ,verbose_name='enter the price')

    category = models.ForeignKey(Category, on_delete=models.CASCADE,
        related_name="products",)
    
    def __str__(self):
        return f"{self.name} — {self.price} cом"