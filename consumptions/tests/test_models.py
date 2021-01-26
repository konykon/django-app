from django.test import TestCase

from consumptions.models import Consumption, Product_Category, Product

class Product_CategoryModelTest(TestCase):
    def setUp(self):
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity=10)

    def test_product_category_code_max_length(self):
        product_category = Product_Category.objects.get(id=1)
        max_length = product_category._meta.get_field('code').max_length
        self.assertEqual(max_length, 200)

    def test_product_category_name_string_code(self):
        self.assertEqual(str(self.prod_cat), 'LL')

    def test_product_category_name_string_name(self):
        self.assertEqual(str(self.prod_cat.name), 'landline')

    def test_product_category_name_string_code(self):
        self.assertEqual(str(self.prod_cat), 'LL')

    def test_product_category_name_string_name(self):
        self.assertEqual(str(self.prod_cat.name), 'landline')
