from django.test import TestCase

from website.models import Contact
from website.forms import ContactForm


class TestContactForm(TestCase):
    """These views tests the contact form."""
    def test_valid_form(self):
        w = Contact.objects.create(name='test user', email='test@test.com', phone='0711 731 771',
                                   subject='Testing form', message='testing contact form')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = Contact.objects.create(name='', email='', phone='', subject='', message='')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_name_missing(self):
        w = Contact.objects.create(name='', email='test@test.com', phone='0711 731 771',
                                   subject='Testing form', message='testing contact form')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_subject_missing(self):
        w = Contact.objects.create(name='test user', email='test@test.com', phone='0711 731 771',
                                   subject='', message='testing contact form')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_phone_missing(self):
        w = Contact.objects.create(name='test user', email='test@test.com', phone='',
                                   subject='Testing form', message='testing contact form')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_message_missing(self):
        w = Contact.objects.create(name='test user', email='test@test.com', phone='0711 731 771',
                                   subject='Testing form', message='')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())

    def test_invalid_form_email_missing(self):
        w = Contact.objects.create(name='test user', email='', phone='0711 731 771',
                                   subject='Testing form', message='testing contact form')
        data = {'name': w.name, 'email': w.email, 'phone': w.phone, 'subject': w.subject,
                'message': w.message, }
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())
