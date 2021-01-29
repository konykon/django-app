from django.test import TestCase

from consumptions.models import Consumption, Product_Category, Product
from .factories import Consumption_Factory, Product_Category_Factory, Product_Factory


product_category = Product_Category_Factory()
product = Product_Factory()
consumption = Consumption_Factory()


class Product_CategoryModelTest(TestCase):
    def test_product_category_strings(self):
        """Test product category name and code are strings"""
        self.assertEqual(product_category.name, 'Landline')
        self.assertEqual(product_category.code, 'LL')

    def test_product_strings(self):
        """Test product name and code are strings"""
        self.assertEqual(product.code, 'LL001')
        self.assertEqual(product.name, 'ADSL')

    def test_consumption_quantity_is_int(self):
        """Test quantity is integer"""
        self.assertEqual(consumption.quantity, 10)

    def test_product_category_is_instance(self):
        """Test product category is created"""
        self.assertTrue(isinstance(product_category, Product_Category))

    def test_product_is_instance(self):
        """Test product is created"""
        self.assertTrue(isinstance(product, Product))

    def test_consumption_is_instance(self):
        """Test consumption is created"""
        self.assertTrue(isinstance(consumption, Consumption))
