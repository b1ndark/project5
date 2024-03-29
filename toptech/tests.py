from django.test import TestCase, Client


class TestPrivacyPolicyView(TestCase):
    def test_privacy_policy_view(self):
        '''
        To Test Privacy Policy page
        '''
        client = Client()
        response = self.client.get('/privacy_policy/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'privacy_policy/privacy_policy.html')
        self.assertContains(
            response, 'https://toptech-244e7b312287.herokuapp.com/')
