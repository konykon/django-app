from django.test import SimpleTestCase, TestCase
from django.urls import path, reverse, resolve
from rest_framework import status
from rest_framework.test import APIClient
from consumptions.models import Consumption, Product, Product_Category
from consumptions.serializers import ConsumptionSerializer
from consumptions.views import *


CONSUMPTIONS_URL = reverse('consumptions:consumption-list')


def sample_product_category(**params):
    """Create and return a sample product category"""
    defaults = {
        'code': 'AA',
        'name': 'testname'
    }
    defaults.update(params)

    return Product_Category.objects.create(**defaults)

def sample_product(**params):
    """Create and return a sample product"""
    defaults = {
        'code': 'AA001',
        'name': 'testproductname',
        'category': sample_product_category()
    }
    defaults.update(params)

    return Product.objects.create(**defaults)

def sample_consumption(**params):
    """Create and return a sample consumption"""
    # import pdb; pdb.set_trace()
    defaults = {
        'product': sample_product(),
        'quantity': 10
    }
    defaults.update(params)

    return Consumption.objects.create(**defaults)

class TestUrls(TestCase):

    def setUp(self):
        self.client = APIClient()
        # self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        # self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        # self.cons = Consumption.objects.create(product=self.prod, quantity='10')

    def test_retrieve_consumptions(self):
        """Test retrieving a list of consumptions"""
        sample_consumption()

        res = self.client.get(CONSUMPTIONS_URL)

        consumptions = Consumption.objects.all().order_by('-id')
        serializer = ConsumptionSerializer(consumptions, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_index_url_is_resolved(self):
        url = reverse('consumptions:index')
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEquals(resolve(url).func.view_class, Index)

    def test_create_url_is_resolved(self):
        url = reverse('consumptions:consumption_create')
        self.assertEquals(resolve(url).func.view_class, ConsumptionCreate)

    def test_upload_product_csv_url_is_resolved(self):
        url = reverse('consumptions:upload_product_csv')
        self.assertEquals(resolve(url).func, upload_product_csv)

    
# class TestUrlsWithArgs(TestCase):

#     def setUp(self):
#         self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
#         self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
#         self.cons = Consumption.objects.create(product=self.prod, quantity='10')

#     def test_update_url_is_resolved(self):
#         url = reverse('consumption_update', kwargs={'pk': 1})
#         print(resolve(url))
#         self.assertEquals(resolve(url).func.view_class, ConsumptionUpdate)

#     def test_delete_url_is_resolved(self):
#         url = reverse('consumption_delete', kwargs={'pk': 1})
#         print(resolve(url))
#         self.assertEquals(resolve(url).func.view_class, ConsumptionDelete)