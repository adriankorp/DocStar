from django.contrib.auth.views import LoginView
from django.shortcuts import render


# Create your views here.



class MyPasswordChangeView(PasswordChangeView):
    template_name = 'form.html'
    success_url = reverse_lazy('doc')


class SignUpView(CreateView):
    template_name = 'form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('doc')


class MyLoginView(LoginView):
    template_name = 'form_login.html'
