from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core import mail

from website.models import Contact


class TestTemplates(TestCase):
    """These tests are aimed at checking template rendering. The tests also check if the context contains the correct 
    data and renders the correct template. """

    # Test homepage rendering
    def test_home_page(self):
        text = "Home"
        template_name = 'website/index.html'
        response = self.client.get("")
        self.assertContains(response, text, count=None, status_code=200)
        self.assertTemplateUsed(response, template_name, count=None)

    # Test about page rendering
    def test_about_page(self):
        text = "About"
        template_name = 'website/about.html'
        response = self.client.get("/about/")
        self.assertContains(response, text, count=None, status_code=200)
        self.assertTemplateUsed(response, template_name, count=None)

    # Test services page rendering
    def test_services_page(self):
        text = "Services"
        template_name = 'website/services.html'
        response = self.client.get("/services/")
        self.assertContains(response, text, count=None, status_code=200)
        self.assertTemplateUsed(response, template_name, count=None)

    # Test support page rendering
    def test_support_page(self):
        text = "Support"
        template_name = 'website/support.html'
        response = self.client.get("/support/")
        self.assertContains(response, text, count=None, status_code=200)
        self.assertTemplateUsed(response, template_name, count=None)

    # Test contact page rendering
    def test_contact_page(self):
        text = "Contact"
        template_name = 'website/contact.html'
        response = self.client.get("/contact/")
        self.assertContains(response, text, count=None, status_code=200)
        self.assertTemplateUsed(response, template_name, count=None)

    # Test success page rendering
    def test_success_page(self):
        text = "Success"
        template_name = 'website/success.html'
        response = self.client.get("/success/")
        self.assertContains(response, text, count=None, status_code=200)
        self.assertTemplateUsed(response, template_name, count=None)


class TestViews(TestCase):
    """ Test reverse urls for views. """
    def test_home_reverse(self):
        url = reverse("website:home")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_reverse(self):
        url = reverse("website:about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_services_reverse(self):
        url = reverse("website:services")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_support_reverse(self):
        url = reverse("website:support")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_contact_reverse(self):
        url = reverse("website:contact")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_success_reverse(self):
        url = reverse("website:success")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)


class TestContactEmail(TestCase):
    """This view tests the contact view email functionality"""
    def test_send_email(self):
        # Send message.
        w = Contact.objects.create(name='test user', email='test@test.com', phone='0711 731 771',
                                   subject='Testing form', message='testing contact form')
        subject = " Testing Message on Contact Form "
        message = 'Testing email functionality on website. \n'
        message += 'Name: ' + w.name + '\n'
        message += 'Subject: ' + w.subject + '\n'
        message += 'Email: ' + w.email + '\n'
        message += 'Phone: ' + w.phone + '\n'
        message += 'Message:\n ' + w.message + '\n'
        mail.send_mail(subject, message, 'anntelebiz@gmail.com', ['anna@anntele.com'], fail_silently=False, )
        url = reverse("website:success")
        response = self.client.get(url)
        # Test that one message has been sent.
        self.assertEqual(len(mail.outbox), 1)
        # Verify that the subject of the first message is correct.
        self.assertEqual(mail.outbox[0].subject, subject)
        self.assertEqual(response.status_code, 200)
