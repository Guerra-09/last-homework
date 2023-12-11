from django.shortcuts import render
from .models import UserProfile
from django.views.generic import CreateView
# Create your views here.

class SignUpView(CreateView):
    model = UserProfile
    template_name = 'registration/signup.html'
    fields = ['name', 'last_name', 'user']
    success_url = '/accounts/login'