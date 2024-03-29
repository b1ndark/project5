from django.test import TestCase
from .models import Product
from django.shortcuts import reverse


class TestProductsView(TestCase):
    @classmethod
    def setUpTestData(cls):
        '''
        To create a product
        '''
        cls.product = Product.objects.create(
            name='playstation',
            price='450.00',
            description='Hello World',
            id=150
        )

    def test_products_view(self):
        '''
        To Test products page
        '''
        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertContains(response, 'playstation')
        self.assertContains(response, '450.00')

    def test_product_detail_view(self):
        '''
        To Test product detail page
        '''
        response = self.client.get(reverse('product_detail', args=[150]))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertContains(response, 'playstation')
        self.assertContains(response, '450.00')
        self.assertContains(response, 'Hello World')
