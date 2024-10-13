"""
David Alvarado
Cis 218
10/12/24
"""

from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    """Model representing a restaurant."""

    name = models.CharField(max_length=200)  # Name of the restaurant
    address = models.CharField(max_length=300)  # Address of the restaurant

    def __str__(self):
        """Return the string representation of the restaurant."""
        return self.name


class Review(models.Model):
    """Model representing a review for a restaurant."""

    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name="reviews")  # Link to Restaurant
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to User who made the review
    rating = models.IntegerField()  # Rating out of 5
    comment = models.TextField()  # User's comment

    def __str__(self):
        """Return a formatted string repressenting the review."""
        return f"{self.user.username}'s review of {self.restaurant.name}"
