from django.test import TestCase, Client


class TestBasketView(TestCase):
    def test_basket_view(self):
        '''
        To Test basket page
        '''
        client = Client()
        response = self.client.get('/basket/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')
        self.assertContains(response, '<span> Keep Shopping</span>')
