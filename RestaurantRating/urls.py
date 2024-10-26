"""
David Alvarado
Cis 218
10/12/24
"""

from django.urls import path 
from accounts.views import SignUpView
from .views import (
    RestaurantListView, 
    RestaurantDetailView, 
    ReviewListView, 
    ReviewDetailView, 
    ReviewCreateView, 
    ReviewUpdateView, 
    ReviewDeleteView,
    SignUpView,
)

urlpatterns = [
    path('', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurant/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'), 
    path('reviews/', ReviewListView.as_view(), name='review_list'), 
    path('review/<int:pk>/', ReviewDetailView.as_view(), name='review_detail'),  
    path('restaurant/<int:restaurant_pk>/review/add/', ReviewCreateView.as_view(), name='add_review'),
    path('review/<int:pk>/update/', ReviewUpdateView.as_view(), name='update_review'), 
    path('review/<int:pk>/delete/', ReviewDeleteView.as_view(), name='delete_review'),  
    path('signup/', SignUpView.as_view(), name='signup'),  
]
