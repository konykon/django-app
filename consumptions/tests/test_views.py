from django.test import TestCase
from django.urls import reverse
import json
from rest_framework import status
from rest_framework.test import APIClient
from consumptions.models import Product_Category, Product


class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_index_view(self):
        """Test retrieving the home page"""
        res = self.client.get(reverse('consumptions:index'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'index.html')

    def test_consumption_table_view(self):
        """Test retrieving a consumptions list"""
        res = self.client.get(reverse('consumptions:consumption_list'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_list.html')

    def test_consumption_create_view(self):
        """Test retrieving the create view"""
        res = self.client.get(reverse('consumptions:consumption_create'))
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_form.html')

    def test_create_consumption(self):
        """Test consumption creating"""
        prod_cat = Product_Category(code='AA', name='adsl')
        prod_cat.save()
        prod = Product(code='AA00', name='aproduct', category=prod_cat)
        prod.save()
        data = json.dumps({
            'product': prod.id,
            'quantity': 10
        })
        response = self.client.post('/consumptions-api/', data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
