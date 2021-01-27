from django.test import TestCase

from consumptions.models import Consumption, Product_Category, Product

class Product_CategoryModelTest(TestCase):
    def setUp(self):
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity=10)

    def test_product_category_name_string_name(self):
        self.assertEqual(str(self.prod_cat.name), 'landline')

    def test_product_category_name_string_code(self):
        self.assertEqual(str(self.prod_cat), 'LL')

    def test_product_category_name_string_name(self):
        self.assertEqual(str(self.prod_cat.name), 'landline')
  
    def test_product_string(self):
        """Test product name and code are strings"""
        self.assertEqual(self.prod.code, 'LL001')
        self.assertEqual(self.prod.name, 'ADSL')

    def test_product_is_instance(self):
        """Tests product is created"""
        self.assertTrue(isinstance(self.prod, Product))

    def test_product_is_instance(self):
        """Test consumption is created"""
        self.assertTrue(isinstance(self.cons, Consumption))
