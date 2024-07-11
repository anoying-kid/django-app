from django.test import TestCase
from django.urls import reverse
from .models import Book

# Create your tests here.
class BookTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.book = Book.objects.create(
            title='This is title',
            subtitle='This is subtitle',
            author='Author Name',
            isbn='23456789'
        )

    def test_book_content(self):
        self.assertEqual(self.book.title, 'This is title')
        self.assertEqual(self.book.subtitle, 'This is subtitle')
        self.assertEqual(self.book.author, 'Author Name')
        self.assertEqual(self.book.isbn, '23456789')
    
    def test_book_listview(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'is subtitle')
        self.assertTemplateUsed(response, 'books/book_list.html')