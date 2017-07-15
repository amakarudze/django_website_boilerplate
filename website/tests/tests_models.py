from django.test import TestCase
from django.utils import timezone

from website.models import Contact


class TestContactModel(TestCase):
    # models test
    def create_contact(self):
        return Contact.objects.create(name="test user", phone="+263771711731", email="test@test.com",
                                      subject="test", message="test message", emaildate=timezone.now())

    def test_contact_creation(self):
        w = self.create_contact()
        self.assertTrue(isinstance(w, Contact))
        self.assertEqual(w.__str__(), w.name)
