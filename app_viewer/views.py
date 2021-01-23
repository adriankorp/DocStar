from django.core.mail import send_mail
from django.http import HttpResponse, BadHeaderError
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import TemplateView

from app_viewer.forms import ContactForm


class HomePage(TemplateView):
    template_name = "home_page.html"


class DocumentView(TemplateView):
    template_name = "documents.html"


class SendDocView(TemplateView):
    template_name = "send_doc.html"


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            name = form.cleaned_data['name']
            from_email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = f'{message} \n Imie: {name} \n Wyslal z emaila: {from_email}'
            try:
                send_mail(subject, message, 'sda.doc.star@gmail.com', ['sda.doc.star@gmail.com'])

            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponse('Thanks for contacting us!')
    return render(request, "contact.html", {'form': form})


class AboutView(TemplateView):
    template_name = "about_as.html"
