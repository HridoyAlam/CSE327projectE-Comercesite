from django.test import TestCase, SimpleTestCase
from django.shortcuts import reverse

# Create your tests here.

#from django.test import TestCase

# class ViewsTestCase(TestCase):
#     def test_index_loads_properly(self):
#         """The index page loads properly"""
#         response = self.client.get('127.0.0.1:8000')
#         self.assertEqual(response.status_code, 200)
#         # self.assertEqual(response.status_code, 404)

class ViewPageTests(SimpleTestCase):

      def test_index_status_code(self):
           response = self.client.get('/')
           self.assertEquals(response.status_code, 200)

      def test_index_url_name(self):
           response = self.client.get(reverse('ShopHome'))
           self.assertEquals(response.status_code, 200)

      def test_correct_template(self):
           response = self.client.get(reverse('ShopHome'))
           self.assertEquals(response.status_code, 200)
           self.assertEquals(response, 'index.html')
