from django.contrib.auth.views import LoginView
from django.shortcuts import render


# Create your views here.


class MyLoginView(LoginView):
    template_name = 'form_login.html'
