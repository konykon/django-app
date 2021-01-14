from django.db import models

# Create your models here.

class Product_Category(models.Model):
    code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)

    class Meta:
        # Gives the proper plural name for admin
        verbose_name_plural = "Product_Categories"

    def __str__(self):
        return self.code

class Product(models.Model):
    code = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Product_Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Consumption(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
