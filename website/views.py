from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

from datetime import datetime

from .forms import ContactForm
from .models import Contact


class HomeView(TemplateView):
    # Renders the homepage
    template_name = 'website/index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['title'] = 'Home'
        context['year'] = datetime.now().year
        return context


class AboutView(TemplateView):
    # Renders the about page
    template_name = 'website/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context['title'] = 'About'
        context['year'] = datetime.now().year
        return context


class ServicesView(TemplateView):
    # Renders the services page
    template_name = 'website/services.html'

    def get_context_data(self, **kwargs):
        context = super(ServicesView, self).get_context_data(**kwargs)
        context['title'] = 'Services'
        context['year'] = datetime.now().year
        return context


class SupportView(TemplateView):
    # Renders the support page
    template_name = 'website/support.html'

    def get_context_data(self, **kwargs):
        context = super(SupportView, self).get_context_data(**kwargs)
        context['title'] = 'Support'
        context['year'] = datetime.now().year
        return context


class ContactView(TemplateView):
    # Renders the contact page
    contact_form = ContactForm()
    template_name = 'website/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        context['title'] = 'Contact'
        context['year'] = datetime.now().year
        context['contact_form'] = self.contact_form
        return context

    def post(self, request):
        if request.method == 'POST':
            contact_form = ContactForm(request.POST)
            obj = Contact()  # gets new object

            if contact_form.is_valid():
                # process the data in contact_form.cleaned_data as required
                obj.name = contact_form.cleaned_data['name']
                obj.subject = contact_form.cleaned_data['subject']
                obj.message = contact_form.cleaned_data['message']
                obj.email = contact_form.cleaned_data['email']
                obj.phone = contact_form.cleaned_data['phone']
                # finally save the object in db
                obj.save()

                # send email to test@test.com -- replace with intended recipient
                subject = "Message on Contact Form "
                message = 'A message was submitted on the website\n\n'
                message += 'Name: ' + obj.name + '\n'
                message += 'Subject: ' + obj.subject + '\n'
                message += 'Email: ' + obj.email + '\n'
                message += 'Phone: ' + obj.phone + '\n'
                message += 'Message:\n ' + obj.message + '\n'

                sender = 'user@test.com' # replace with configured email account in settings.py

                recipient_list = ['test@test.com'] # replace with intenced recipient(s)
                send_mail(subject, message, sender, recipient_list)

                # send auto-response to email sender
                recipient_list = [obj.email]
                message = 'Thank you for the email you sent on our website. We will get back to you soon.'
                # you can change the sender here if you have another email account configured in settings.py
                send_mail(subject, message, sender, recipient_list)

                # redirect to a new URL:
                return HttpResponseRedirect(reverse('website:success'))
            else:
                contact_form = ContactForm()
                return render(request, 'website/contact.html', {'contact_form': contact_form})


class SuccessView(TemplateView):
    template_name = 'website/success.html'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['title'] = 'Success'
        context['year'] = datetime.now().year
        return context