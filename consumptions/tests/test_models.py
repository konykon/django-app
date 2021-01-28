from django.test import TestCase

from consumptions.models import Consumption, Product_Category, Product
from .factories import (Consumption_Factory, Product_Category_Factory,
                        Product_Factory)


class Product_CategoryModelTest(TestCase):
    def test_product_category_strings(self):
        """Test product category name and code are strings"""
        self.assertEqual(Product_Category_Factory().name, 'Landline')
        self.assertEqual(Product_Category_Factory().code, 'LL')

    def test_product_strings(self):
        """Test product name and code are strings"""
        self.assertEqual(Product_Factory().code, 'LL001')
        self.assertEqual(Product_Factory().name, 'ADSL')

    def test_consumption_quantity_is_int(self):
        """Test quantity is integer"""
        self.assertEqual(Consumption_Factory().quantity, 10)

    def test_product_category_is_instance(self):
        """Test product category is created"""
        self.assertTrue(isinstance(
            Product_Category_Factory(), Product_Category)
        )

    def test_product_is_instance(self):
        """Test product is created"""
        self.assertTrue(isinstance(Product_Factory(), Product))

    def test_consumption_is_instance(self):
        """Test consumption is created"""
        self.assertTrue(isinstance(Consumption_Factory(), Consumption))
