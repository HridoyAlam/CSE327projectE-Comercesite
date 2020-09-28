from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pylint.test.functional.undefined_variable import Self
from shop.views import index


from eab.views import index

class TestUrls(SimpleTestCase):

    def test_urls_is_resolved(self):
        url = reverse('ShopHome')
        print(resolve(url))
