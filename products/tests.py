from django.test import TestCase, Client


class TestProductsView(TestCase):
    def test_products_view(self):
        '''
        To Test products page
        '''
        client = Client()
        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
