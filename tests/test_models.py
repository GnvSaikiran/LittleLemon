from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_add_item(self):
        item = Menu.objects.create(title="Tempura", price=8, inventory=8)
        self.assertEqual(item.title, "Tempura")