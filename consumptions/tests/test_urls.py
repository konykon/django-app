from django.test import SimpleTestCase, TestCase
from django.urls import path, reverse, resolve
from consumptions.views import *

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('consumptions:index')
        self.assertEquals(resolve(url).func.view_class, Index)

    def test_list_url_is_resolved(self):
        url = reverse('consumptions:consumption_list')
        self.assertEquals(resolve(url).func.view_class, ConsumptionList)

    def test_create_url_is_resolved(self):
        url = reverse('consumptions:consumption_create')
        self.assertEquals(resolve(url).func.view_class, ConsumptionCreate)

    def test_upload_csv_url_is_resolved(self):
        url = reverse('consumptions:upload_product_csv')
        self.assertEquals(resolve(url).func, upload_product_csv)

    
class TestUrlsWithArgs(TestCase):

    def setUp(self):
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity='10')

    def test_delete_url_is_resolved(self):
        url = reverse('consumptions:consumption_delete', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, ConsumptionDelete)