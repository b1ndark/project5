from django.test import TestCase, Client


class TestContactView(TestCase):
    def test_contact_view(self):
        '''
        To Test contact page
        '''
        client = Client()
        response = self.client.get('/contact/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/contact.html')
        self.assertContains(response, 'Contact form')
