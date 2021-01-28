from django.contrib import admin
from .models import Consumption, Product_Category, Product

# Register your models here.
admin.site.register(Product_Category)
admin.site.register(Product)
admin.site.register(Consumption)
