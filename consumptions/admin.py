from django.contrib import admin
from .models import Consumption, Product_Category, Product
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class ProductCategoryResource(resources.ModelResource):
    class Meta:
        model = Product_Category


class ProductResource(resources.ModelResource):
    class Meta:
        model = Product


class Product_CategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ProductCategoryResource


class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = ProductResource


# Register your models here.
admin.site.register(Product_Category, Product_CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consumption)