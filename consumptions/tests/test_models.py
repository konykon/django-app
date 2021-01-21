from django.test import TestCase

from consumptions.models import Consumption, Product_Category, Product

class Product_CategoryModelTest(TestCase):
    def setUp(self):
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity=10)

    def test_product_category_string(self):
        """Test product category name and code are strings"""
        self.assertEqual(Product_Category_Factory().code, 'LL')
        self.assertEqual(Product_Category_Factory().name, 'Landline')

    def test_product_category_is_instance(self):
        """Tests product category is created"""
        self.assertTrue(isinstance(Product_Category_Factory(), Product_Category))


class Product_ModelTest(TestCase):

    def test_product_string(self):
        """Test product name and code are strings"""
        self.assertEqual(Product_Factory().code, 'LL001')
        self.assertEqual(Product_Factory().name, 'ADSL')

    def test_product_is_instance(self):
        """Tests product is created"""
        self.assertTrue(isinstance(Product_Factory(), Product))


class Consumption_ModelTest(TestCase):

    def test_product_is_instance(self):
        """Test consumption is created"""
        self.assertTrue(isinstance(Consumption_Factory(), Consumption))

