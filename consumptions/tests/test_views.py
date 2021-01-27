from django.test import TestCase, Client
from django.urls import reverse
from consumptions.models import *
import json

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity=10)

    def test_index_get(self):
        response = self.client.get(reverse('consumptions:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_consumption_table_get(self):
        response = self.client.get(reverse('consumptions:consumption_list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'consumption_list.html')

    def test_consumption_create_get(self):
        response = self.client.get(reverse('consumptions:consumption_create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'consumption_form.html')


    def test_consumption_delete_delete(self):
        response = self.client.delete(reverse('consumptions:consumption_delete', kwargs={'pk': self.cons.pk}))
        self.assertEquals(response.status_code, 302)
