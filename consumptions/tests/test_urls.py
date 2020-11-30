from django.test import SimpleTestCase, TestCase
from django.urls import path, reverse, resolve
from consumptions.views import *

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('index')
        print(resolve(url))
        self.assertEquals(resolve(url).func, index)

    def test_api_list_url_is_resolved(self):
        url = reverse('api')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionApi)

    def test_api_create_url_is_resolved(self):
        url = reverse('api_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionCreateApi)

    def test_list_url_is_resolved(self):
        url = reverse('consumptions')
        print(resolve(url))
        self.assertEquals(resolve(url).func, filter_by_product_category)

    def test_create_url_is_resolved(self):
        url = reverse('consumption_create')
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionCreate)

    def test_upload_csv_url_is_resolved(self):
        url = reverse('upload_product_categories_csv')
        print(resolve(url))
        self.assertEquals(resolve(url).func, upload_product_categories_csv)

    
class TestUrlsWithArgs(TestCase):

    def setUp(self):
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity='10')

    def test_update_url_is_resolved(self):
        url = reverse('api_update', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionUpdateApi)

    def test_update_api_url_is_resolved(self):
        url = reverse('api_delete', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionDeleteApi)

    def test_delete_api_url_is_resolved(self):
        url = reverse('consumption_update', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionUpdate)

    def test_delete_url_is_resolved(self):
        url = reverse('consumption_delete', kwargs={'pk': 1})
        print(resolve(url))
        self.assertEquals(resolve(url).func.view_class, ConsumptionDelete)