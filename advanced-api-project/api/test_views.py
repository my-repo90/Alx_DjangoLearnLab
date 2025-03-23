from rest_framework.test import APIRequestFactory
from django.test import TestCase
from rest_framework.test import APITestCase
from .models import Book

class BookAPITestCase(APITestCase):
    def setUp(self):   
        self.client.login(username="testuser", password="testpassword")
   
    def test_books_response(self):
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, 200)



    # ["self", "class", "APITestCase"]
    #["from rest_framework import status", "response.data"]
    #["self.client.login"]
