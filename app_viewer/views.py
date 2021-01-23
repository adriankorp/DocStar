from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "home_page.html"


class DocumentView(TemplateView):
    template_name = "documents.html"


class SendDocView(TemplateView):
    template_name = "send_doc.html"


class ContactView(TemplateView):
    template_name = "contact.html"


class AboutView(TemplateView):
    template_name = "about_as.html"
