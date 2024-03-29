from django.test import TestCase
from .models import About


class TestAboutView(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        To create about
        '''
        cls.about = About.objects.create(
            name='adamyuri',
        )

    def test_about_view(self):
        '''
        To Test about page
        '''
        response = self.client.get('/about/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about/about.html')
        self.assertContains(response, 'About Us')
        self.assertContains(response, 'adamyuri')
