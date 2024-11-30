from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from your_app.models import Book, Author

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Set up initial data for the tests
        self.author = Author.objects.create(name="John Doe")
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )
        self.book_create_url = reverse("book_list_create")  # Adjust the name to match your URL pattern
        self.book_detail_url = reverse("DetailView", kwargs={"pk": self.book.id})

    def test_create_book(self):
        # Test creating a new book
        data = {
            "title": "New Book",
            "publication_year": 2022,
            "author": self.author.id
        }
        response = self.client.post(self.book_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["title"], "New Book")
        self.assertEqual(response.data["publication_year"], 2022)

    def test_update_book(self):
        # Test updating an existing book
        update_url = reverse("DetailView", kwargs={"pk": self.book.id})
        data = {"title": "Updated Book Title"}
        response = self.client.patch(update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Updated Book Title")

    def test_delete_book(self):
        # Test deleting a book
        delete_url = reverse("DetailView", kwargs={"pk": self.book.id})
        response = self.client.delete(delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify the book is deleted
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

    def test_get_book_detail(self):
        # Test retrieving a book's detail
        response = self.client.get(self.book_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], self.book.title)
        self.assertEqual(response.data["publication_year"], self.book.publication_year)

    def test_get_book_list(self):
        # Test retrieving a list of books
        response = self.client.get(self.book_create_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book_invalid_year(self):
        # Test creating a book with an invalid publication year
        data = {
            "title": "Invalid Year Book",
            "publication_year": 2025,  # Future year
            "author": self.author.id
        }
        response = self.client.post(self.book_create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("publication_year", response.data)
