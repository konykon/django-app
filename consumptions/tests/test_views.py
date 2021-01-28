from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient


class TestViews(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_index_get(self):
        """Test retrieving the home page"""
        res = self.client.get(reverse('consumptions:index'))
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'index.html')

    def test_consumption_table_get(self):
        """Test retrieving a consumptions list"""
        res = self.client.get(reverse(
            'consumptions:consumption_list')
        )
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_list.html')

    def test_consumption_create_get(self):
        """Test retrieving the create view"""
        res = self.client.get(reverse(
            'consumptions:consumption_create')
        )
        self.assertEquals(res.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(res, 'consumption_form.html')
