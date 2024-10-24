"""
David Alvarado
Cis 218
10/12/24
"""

from django.contrib.auth.models import User
from django.db import models

class Restaurant(models.Model):
    """Restaurant Model"""
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    address = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    """Review Model"""
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()  
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Review of {self.restaurant.name} by {self.user.username}"

