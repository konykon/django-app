from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from consumptions.views import (ConsumptionList, ConsumptionCreate, Index,
                                ConsumptionDelete, upload_product_csv)


class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        """Test index url is resolved"""
        url = reverse('consumptions:index')
        self.assertEqual(resolve(url).func.view_class, Index)

    def test_list_url_is_resolved(self):
        """Test consumptions list url is resolved"""
        url = reverse('consumptions:consumption_list')
        self.assertEqual(resolve(url).func.view_class, ConsumptionList)

    def test_create_url_is_resolved(self):
        """Test create consumption url is resolved"""
        url = reverse('consumptions:consumption_create')
        self.assertEqual(resolve(url).func.view_class, ConsumptionCreate)

    def test_upload_csv_url_is_resolved(self):
        """Test upload csv url is resolved"""
        url = reverse('consumptions:upload_product_csv')
        self.assertEqual(resolve(url).func, upload_product_csv)


class TestUrlsWithArgs(TestCase):
    def test_delete_url_is_resolved(self):
        """Test delete consumption url is resolved"""
        url = reverse('consumptions:consumption_delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, ConsumptionDelete)
