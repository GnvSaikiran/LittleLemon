from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.item_one = Menu.objects.create(title="pasta", price=10, inventory=5)
        self.item_two = Menu.objects.create(title="chicken fry", price=15, inventory=15)

    def test_getall(self):
        self.assertEqual(self.item_one.title, 'pasta')
        self.assertEqual(self.item_two.title, 'chicken fry')