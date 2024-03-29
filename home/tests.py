from django.test import TestCase


class TestHomeView(TestCase):
    def test_home_view(self):
        '''
        To Test home page
        '''
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertContains(response, 'Check the latest Tech!')
