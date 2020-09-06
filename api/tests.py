from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from Pin.models import Category, Pin

class CategoryAPITests(APITestCase):

    def test_category_post(self):
        url = '/api/v1/category/'
        data = {'name': 'Костер', 'description': 'None', 'danger': 'None'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)

    def test_category_get(self):
        url = '/api/v1/category/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_category_put(self):
        url = '/api/v1/category/',
        data = {'name': 'Костер', 'description': 'None', 'danger': 'None'}
        response = self.client.put(url,
                                   data,
                                   content_type='application/json', format='json', kwargs={'pk': self.Category.pk},)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PinAPITests(APITestCase):
    """

    def test_pin_post(self):
        url = '/api/v1/'
        data = {"title": "нарушение",
                "geo": "50.039402, 36.310139",
                "category": 1,
                "user": 1,
                "img": "1.png",
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pin.objects.count(), 1)
    """

    def test_category_get(self):
        url = '/api/v1/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
