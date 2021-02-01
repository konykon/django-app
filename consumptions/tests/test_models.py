from django.test import TestCase
from django.db.utils import IntegrityError
from datetime import datetime
from consumptions.models import Consumption, Product_Category, Product
from .factories import Consumption_Factory, Product_Category_Factory, Product_Factory


class Product_CategoryModelTest(TestCase):

    def setUp(self):
        self.product_category = Product_Category_Factory()
        self.product = Product_Factory()
        self.consumption = Consumption_Factory()

    def test_product_category_strings(self):
        """Test product category name and code are strings"""
        self.assertEqual(self.product_category.name, 'Landline')
        self.assertEqual(self.product_category.code, 'LL')

    def test_product_strings(self):
        """Test product name and code are strings"""
        self.assertEqual(self.product.code, 'LL001')
        self.assertEqual(self.product.name, 'ADSL')

    def test_consumption_timestamp(self):
        """Test consumption timestamp"""
        timestamp = self.consumption.timestamp.isoformat(timespec='minutes')
        self.assertEqual(timestamp, datetime.now().isoformat(timespec='minutes'))

    def test_product_category_is_instance(self):
        """Test product category is created"""
        self.assertTrue(isinstance(self.product_category, Product_Category))

    def test_product_is_instance(self):
        """Test product is created"""
        self.assertTrue(isinstance(self.product, Product))

    def test_consumption_is_instance(self):
        """Test consumption is created"""
        self.assertTrue(isinstance(self.consumption, Consumption))

    def test_duplicate_product_categories_are_invalid(self):
        """Test product category is unique"""
        Product_Category.objects.create(code='AA', name='adsl')
        self.assertRaises(IntegrityError, Product_Category.objects.create, code='AA', name='adsl')

    def test_duplicate_products_are_invalid(self):
        """Test product is unique"""
        p_c = Product_Category.objects.create(code='AA', name='adsl')
        Product.objects.create(code='AA', name='aproduct', category=p_c)
        self.assertRaises(IntegrityError, Product.objects.create, code='AA', name='aproduct', category=p_c)

    def test_why_this_test_pass(self):
        """I didn't create a product outside of assertRaises. Factory boy saves instances?"""
        prod_cat = Product_Category_Factory().save()
        self.assertRaises(IntegrityError, Product.objects.create, code='AA', name='aproduct', category=prod_cat)
