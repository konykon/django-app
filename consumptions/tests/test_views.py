from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from consumptions.models import *
import json


CONSUMPTIONS_URL = reverse('consumptions:consumption-list')


class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.prod_cat = Product_Category.objects.create(code='LL', name='landline')
        self.prod = Product.objects.create(code='LL001', name='ADSL', category=self.prod_cat)
        self.cons = Consumption.objects.create(product=self.prod, quantity=10)

    def test_consumptions_list_get(self):
        """Test list of consumptions render and view"""
        res = self.client.get(reverse('consumptions:consumption_list'))
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_list.html')

    def test_consumption_create_get(self):
        """Test consumptions create render and view"""
        res = self.client.get(reverse('consumptions:consumption_create'))
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_form.html')

#     def test_consumption_create_post(self):
#         response = self.client.post(reverse('consumption_create'), {
#             'product': 'LL001', 
#             'quantity': 10
#         })
#         self.assertEquals(response.status_code, 302)
#         self.assertEquals(self.prod.code, 'LL001')


#     def test_consumption_delete_delete(self):
#         response = self.client.delete(reverse('consumption_delete', kwargs={'pk': self.cons.pk}))
#         self.assertEquals(response.status_code, 302)



