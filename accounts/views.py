"""
David Alvarado
Cis 218
10/12/24
"""

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView



class SignUpView(CreateView):
    """User Sign Up View"""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
    
    def form_valid(self, form):
        """If the form is valid, save the user and redirect to the login page."""
        response = super().form_valid(form)
        form.save()  # save the form data to create a new user
        return response