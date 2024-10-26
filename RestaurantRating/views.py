"""
David Alvarado
Cis 218
10/12/24
"""
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Restaurant, Review
from django.contrib.auth.forms import UserCreationForm  
from django.urls import reverse_lazy
from accounts.views import SignUpView
from django.urls import reverse

# List all restaurants
class RestaurantListView(ListView):
    """Restaurant List View"""
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = "restaurants"

# Detail view for a single restaurant
class RestaurantDetailView(DetailView):
    """Restaurant Detail View"""
    model = Restaurant
    template_name = 'restaurant_detail.html'
    context_object_name = "restaurant"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # gets all reviews related to this restaurant using the related_name
        context['reviews'] = self.object.reviews.all()  # Use related_name 'reviews'
        return context

# List of reviews for a specific restaurant
class ReviewListView(ListView):
    """Review List View"""
    model = Review
    template_name = 'review_list.html'
    context_object_name = "reviews"

# Detail view for a specific review
class ReviewDetailView(DetailView):
    """Review Detail View"""
    model = Review
    template_name = 'review_detail.html'
    context_object_name = "review"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # gets all reviews related to this restaurant using the related_name
        context['reviews'] = self.object.reviews.all()  # Use related_name 'reviews'
        return context

# Create a new review
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
        """gets the restaurant and passes it to the context"""
        context = super().get_context_data(**kwargs)
        context['restaurant'] = Restaurant.objects.get(pk=self.kwargs['restaurant_pk'])
        return context

    def get_success_url(self):
        return reverse('restaurant_detail', kwargs={'pk': self.kwargs['restaurant_pk']})# Redirect to the restaurant detail page after successful submission

# Update a review
class ReviewUpdateView(LoginRequiredMixin, UpdateView):
    """Review Update View"""
    model = Review
    template_name = 'review_form.html'
    fields = ['body', 'rating']

# Delete a review
class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    """Review Delete View"""
    model = Review
    template_name = 'review_confirm_delete.html'
    success_url = '/'