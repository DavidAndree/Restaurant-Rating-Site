"""
David Alvarado
Cis 218
10/12/24
"""

from django.test import TestCase
from django.urls import reverse
from .models import Restaurant, Review
from django.contrib.auth.models import User
from django.db.models import Avg

class RestaurantModelTests(TestCase):
    """Tests for the Restaurant model."""

    def test_str(self):
        """Test the string representation of the Restaurant model."""
        restaurant = Restaurant.objects.create(name="Test Restaurant")
        self.assertEqual(str(restaurant), "Test Restaurant")

    def test_average_rating(self):
        """Test the average rating calculation of the Restaurant model."""
        restaurant = Restaurant.objects.create(name="Test Restaurant")
        user = User.objects.create_user(username='testuser', password='12345')
        Review.objects.create(restaurant=restaurant, user=user, body="Good", rating=4)
        Review.objects.create(restaurant=restaurant, user=user, body="Okay", rating=2)
        
        avg_rating = restaurant.reviews.aggregate(Avg('rating'))['rating__avg']
        self.assertEqual(avg_rating, 3.0)

class ReviewModelTests(TestCase):
    """Tests for the Review model."""

    def test_str(self):
        """Test the string representation of the Review model."""
        restaurant = Restaurant.objects.create(name="Test Restaurant")
        user = User.objects.create_user(username='testuser', password='12345')
        review = Review.objects.create(restaurant=restaurant, user=user, body="Good place", rating=4)
        self.assertEqual(str(review), f"Review of {restaurant.name} by {user.username}")

class RestaurantViewTests(TestCase):
    """Tests for views related to the Restaurant and Review models."""

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.restaurant = Restaurant.objects.create(name="Test Restaurant")
        self.client.login(username='testuser', password='12345')

    def test_restaurant_list_view(self):
        """Test the restaurant list view."""
        response = self.client.get(reverse('restaurant_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.restaurant.name)

    def test_restaurant_detail_view(self):
        """Test the restaurant detail view."""
        response = self.client.get(reverse('restaurant_detail', args=[self.restaurant.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.restaurant.name)

    def test_create_review_view(self):
        """Test creating a review for a restaurant."""
        response = self.client.post(
            reverse('add_review', args=[self.restaurant.pk]),
            {
                'body': 'Great food!',
                'rating': 5,
            }
        )
        self.assertEqual(response.status_code, 302)  # Redriect after successful post
        self.assertEqual(Review.objects.count(), 1)
        self.assertEqual(Review.objects.first().body, "Great food!")

    def test_review_detail_view(self):
        """Test the review detail view."""
        review = Review.objects.create(restaurant=self.restaurant, user=self.user, body="Good place", rating=4)
        response = self.client.get(reverse('review_detail', args=[review.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, review.body)
