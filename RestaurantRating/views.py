"""
David Alvarado
Cis 218
10/12/24
"""

from django.views import generic
from django.urls import reverse_lazy
from .models import Restaurant, Review
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm


class RestaurantListView(generic.ListView):
    """View to list all restaurants."""

    model = Restaurant
    template_name = "restaurant_list.html"


class RestaurantDetailView(generic.DetailView):
    """View to display details of a single restaurant."""

    model = Restaurant
    template_name = "restaurant_detail.html"


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    """View to create a new review."""

    model = Review
    fields = ["rating", "comment"]
    template_name = "review_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user  # Set the user to the currently logged in user
        form.instance.restaurant_id = self.kwargs["pk"]  # Get restaurant from URL
        return super().form_valid(form)


class ReviewUpdateView(LoginRequiredMixin, generic.UpdateView):
    """View to update an existing review."""

    model = Review
    fields = ["rating", "comment"]
    template_name = "review_form.html"


class ReviewDeleteView(LoginRequiredMixin, generic.DeleteView):
    """View to delete a review."""

    model = Review
    template_name = "review_confirm_delete.html"
    success_url = reverse_lazy("restaurant_list")


class SignUpView(generic.CreateView):
    """View for user signup."""

    form_class = UserCreationForm
    template_name = "signup.html"
    success_url = reverse_lazy("login")
