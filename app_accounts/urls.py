from django.urls import path
from django.contrib.auth.views import LogoutView

from .views import (MyLoginView, MyPasswordChangeView, SignUpView)

app_name = 'accounts'
urlpatterns = [
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', MyPasswordChangeView.as_view(), name='password-change'),
    path('sign-up/', SignUpView.as_view(), name='sign-up')