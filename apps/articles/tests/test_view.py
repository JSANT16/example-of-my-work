from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.articles.tests.test_setup import TestSetUp
from apps.articles.models import Vendor


class TestViews(TestSetUp):

    def test_cannot_create_article_without_data(self):
        """
        Ensure we can't create a new Article without data.
        """
        url = reverse('articles:article-list')
        response = self.client.post(url, self.data, format=self.format)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_can_create_article(self):
        """
        Ensure we can create a new Article with data.
        """
        vendors = Vendor.objects.create(name='Jose', address='CDMX')
        self.data = {
            "code": 1,
            "description": "Mi 11",
            "price": 20000.00,
            "vendors": [vendors.id]
        }
        response = self.client.post(
            reverse('articles:article-list'), self.data, format=self.format)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
