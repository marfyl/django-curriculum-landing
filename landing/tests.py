from django.test import TestCase, Client
from django.urls import reverse


class LandingTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('landing:index')

    def test_landing(self):
        # Do action
        response = self.client.get(self.url)

        # Asserts
        self.assertEqual(response.status_code, 200)

    def test_landing_context(self):
        # Do action
        response = self.client.get(self.url)

        # Asserts
        self.assertIn('ANALYTICS_CODE', response.context_data.keys())
        self.assertIn('form', response.context_data.keys())

    def test_landing_contact_form_valid(self):
        # Do action
        data = {
            'name': 'contact name',
            'email': 'email@example.com',
            'message': 'Hello'
        }
        response = self.client.post(self.url, data)

        # Asserts
        self.assertEqual(response.status_code, 302)

    def test_landing_contact_form_invalid(self):
        # Do action
        data = {
            'name': 'contact name',
            'email': '',
            'message': ''
        }
        response = self.client.post(self.url, data)

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context_data.get('form').is_valid())
