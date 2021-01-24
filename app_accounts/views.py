from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import CreateView
from .forms import (SignUpForm)

# Create your views here.




class SignUpView(CreateView):
    template_name = 'form_sign_up.html'
    form_class = SignUpForm
    success_url = reverse_lazy('app_viewer:home')


class MyLoginView(LoginView):
    template_name = 'form_login.html'
