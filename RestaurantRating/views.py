"""
David Alvarado
Cis 218
10/12/24
"""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from .models import Restaurant, Review
from accounts.views import SignUpView
from django.db.models import Avg

# List all restaurants
class RestaurantListView(ListView):
    """Restaurant List View"""
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = "restaurants"

    def get_queryset(self):
        # Calculates ratig for the list of restaurant
        queryset = super().get_queryset().annotate(avg_rating=Avg('reviews__rating'))
        return queryset  
    
# Detail view for a single restaurant
class RestaurantDetailView(DetailView):
    """Restaurant Detail View"""
    model = Restaurant
    template_name = 'restaurant_detail.html'
    context_object_name = "restaurant"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()
        # Access related reviews through the restaurant object
        context['reviews'] = self.object.reviews.all()
        average_rating = reviews.aggregate(avg_rating=Avg('rating'))['avg_rating']
        context['average_rating'] = average_rating if average_rating else 0.0  # Defaults to 0.0 if there is no rating
        return context


class ReviewListView(ListView):
    """Review List View"""
    model = Review
    template_name = 'review_list.html'
    context_object_name = "reviews"

# Detail view for a specific review
class ReviewDetailView(LoginRequiredMixin, DetailView):
    """Review Detail View"""
    model = Review
    template_name = 'review_detail.html'
    context_object_name = "review"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# Create a new review for a specific restaurant
class ReviewCreateView(LoginRequiredMixin, CreateView):
    """Review Create View"""
    model = Review
    template_name = 'review_form.html'
    fields = ['body', 'rating']

    def form_valid(self, form):
        form.instance.restaurant_id = self.kwargs['restaurant_pk']
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        """Passes the restaurant to the context"""
        context = super().get_context_data(**kwargs)
        context['restaurant'] = Restaurant.objects.get(pk=self.kwargs['restaurant_pk'])
        return context

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.kwargs['restaurant_pk']})

class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """Review Update View"""
    model = Review
    template_name = 'review_form.html'
    fields = ['body', 'rating']

    def get_context_data(self, **kwargs):
        """Pass the restaurant context to the template"""
        context = super().get_context_data(**kwargs)
        context['restaurant'] = self.object.restaurant  # Access the related restaurant
        return context

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.object.restaurant.pk})

# Delete a review
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """Review Delete View"""
    model = Review
    template_name = 'review_confirm_delete.html'

    def get_success_url(self):
        # Redirect to the restaurant detail page after deleting a review
        return reverse('restaurant_detail', kwargs={'pk': self.object.restaurant.pk})