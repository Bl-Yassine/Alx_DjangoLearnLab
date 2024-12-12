from django.shortcuts import render

# Create your views here.

#User Registration
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterUserForm

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'
