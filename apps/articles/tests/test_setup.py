from rest_framework.test import APITestCase


class TestSetUp(APITestCase):
    def setUp(self):
        self.data = {}
        self.format = "json"
        return super().setUp()
