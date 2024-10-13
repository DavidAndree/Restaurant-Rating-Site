"""
David Alvarado
Cis 218
10/12/24
"""

from django.test import TestCase
from .models import Restaurant, Review
from django.contrib.auth.models import User


class RestaurantModelTests(TestCase):
    """Tests for the Restaurant model."""

    def test_str(self):
        restaurant = Restaurant(name="Test Restaurant")
        self.assertEqual(str(restaurant), "Test Restaurant")
