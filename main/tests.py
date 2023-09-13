from django.test import TestCase, Client
from main.models import Item

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

class FruitsTestCase(TestCase):
    def setUp(self):
        Item.objects.create(name='Strawberry', category='fruits', amount=1)
        Item.objects.create(name='Blueberry', category='fruits', amount=5)

    def test_fruits(self):
        """Fruits' categories are correctly identified"""
        strawberry = Item.objects.get(name="Strawberry")
        blueberry = Item.objects.get(name="Blueberry")
        self.assertEqual(strawberry.category, 'fruits')
        self.assertEqual(blueberry.category, 'fruits')