from django.test import TestCase

from .models import Todo

# Create your tests here.
class TodoModelTestCase(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.todo = Todo.objects.create(title='This is django title', body='This is django body')

    def test_model_content(self):
        self.assertEqual(self.todo.title, 'This is django title')
        self.assertEqual(self.todo.body, 'This is django body')
        self.assertEqual(str(self.todo), 'This is django title')