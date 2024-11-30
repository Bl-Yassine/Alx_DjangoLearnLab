from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
class TestCreateBook(APITestCase):

    def test_create_book(self):
        simple_book = {'title':"The World As I See It" ,'publication_year': 1935 , 'author' : 'Albert Einstein'}
        response = self.client.post (reverse('CreateView'), simple_book)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
