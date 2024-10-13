"""
David Alvarado
Cis 218
10/12/24
"""

from django.contrib import admin
from .models import Restaurant, Review

admin.site.register(Restaurant)
admin.site.register(Review)
