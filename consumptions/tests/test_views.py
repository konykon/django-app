from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory
from .factories import Consumption_Factory
from consumptions.views import ConsumptionViewSet


class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.factory = APIRequestFactory()

    def test_index_get(self):
        """Test retrieving the home page"""
        res = self.client.get(reverse('consumptions:index'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'index.html')

    def test_consumption_table_get(self):
        """Test retrieving a consumptions list"""
        res = self.client.get(reverse('consumptions:consumption_list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_list.html')

    def test_consumption_create_get(self):
        """Test retrieving the create view"""
        res = self.client.get(reverse('consumptions:consumption_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_form.html')

    # def test_consumption_create(self):
    #     """Test creating consumption"""
    #     consumption = {
    #         'product': 'LL001',
    #         'quantity': 10
    #     }
    #     request = self.factory.post('/consumptions-api', consumption, format='json')
    #     print(request.body)
    #     view = ConsumptionViewSet
    #     response = view.as_view(actions={'post': 'create'})(request)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_create(self):
    #     data = json.dumps({
    #         'product': 'LL001',
    #         'quantity': 10
    #     })
    #     response = client.post('/consumptions/create/', data=data, content_type='application/json')
    #     # Check if you get a 200 back:
    #     print(response)
    #     self.assertEqual(response.status_code, )
    #     # Check to see if Wishbone was created
    #     self.assertEqual(response.data['results']['product'], 'LL001')
