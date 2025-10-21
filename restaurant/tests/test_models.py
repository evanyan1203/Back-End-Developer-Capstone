from django.test import TestCase
from restaurant.models import Menu

class MenuModelTest(TestCase):

    def setUp(self):
        # Create a Menu object before each test
        self.menu_item = Menu.objects.create(
            name="Pasta",
            price=12,
            menu_item_description="Delicious Italian pasta with cheese"
        )

    def test_menu_item_creation(self):
        """Test that the Menu object is created correctly"""
        self.assertEqual(self.menu_item.name, "Pasta")
        self.assertEqual(self.menu_item.price, 12)
        self.assertEqual(self.menu_item.menu_item_description, "Delicious Italian pasta with cheese")

    def test_str_method_returns_name(self):
        """Test that the __str__ method returns the name"""
        self.assertEqual(str(self.menu_item), "Pasta")