from django.test import TestCase
from .forms import ContactForm


class TestContactForm(TestCase):
    
    def test_name_is_required(self):
        """Test for the 'name' field"""
        form = ContactForm({
            'name': '',
            'subject': 'Yo!',
            'email': 'test@test.com',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    def test_email_is_required(self):
        """Test for the 'email' field"""
        form = ContactForm({
            'name': 'Matt',
            'subject': 'Hi',
            'email': '',
            'message': 'Hello!'
        })
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    def test_message_is_required(self):
        """Test for the 'message' field"""
        form = ContactForm({
            'name': 'Matt',
            'subject': 'Howdy',
            'email': 'test@test.com',
            'message': ''
        })
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )