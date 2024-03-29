from django.test import TestCase
from django.contrib.auth.models import User


class TestProfileView(TestCase):

    @classmethod
    def setUpTestData(cls):
        '''
        To create a user
        '''
        cls.user = User.objects.create(
            email='adam_yuri@test.com',
            username='adamyuri',
            password='pw123456',
        )

    def test_profile_view(self):
        '''
        To Test profile page
        '''
        self.client.force_login(self.user)
        response = self.client.get('/profile/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, "adamyuri's profile")
        self.assertContains(response, 'Personal Information')
        self.assertContains(response, 'Danger')
