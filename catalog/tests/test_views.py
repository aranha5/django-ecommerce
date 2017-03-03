from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from model_mommy import mommy

from catalog.models import Category, Product


class ProductListTestCase(TestCase):

    def setUp(self):
        self.url = reverse('catalog:product_list')
        self.client = Client()
        self.products = mommy.make('catalog.Product', _quantity=10)

    def tearDown(self):
        for p in self.products:
            p.delete()

    def test_view_ok(self):
        responde = self.client.get(self.url)
        self.assetEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'catalog/product_list.html')
