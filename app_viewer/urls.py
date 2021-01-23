"""DocStar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from app_viewer.views import HomePage, DocumentView, SendDocView, ContactView, AboutView

app_name = 'app_viewer'

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('docs/', DocumentView.as_view(), name='docs'),
    path('send_doc/', SendDocView.as_view(), name='doc-send'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about_us/', AboutView.as_view(), name='about'),
]
