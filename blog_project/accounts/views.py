
from django.contrib.auth.forms import UserCreationForm  # Buit-in Django form to create users.
from django.urls import reverse_lazy
from django.views import generic

# We need to write our own view for a sign up page to register new users, but Django provides us with a form class,
# UserCreationForm. By default it comes with three fields: username, password1, and password2.


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')  # reverse_lazy to redirect the user to login page upon successful registration.
    # The reason is that for all generic class-based views the URLs are not loaded when the file is imported, so we have
    # to use the lazy form of reverse to load them later when they’re available
    template_name = 'signup.html'

