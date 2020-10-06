from astroid.protocols import objects
from django.test import TestCase
from django.db import models
from django.contrib.auth import get_user_model
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from pylint.test.functional.undefined_variable import Self

from shop.models import Orders
from shop.views import index
# Create your tests here.
class orderTest(TestCase):


    def setUp(self):
        self.order_id = objects.create_order(order_id="01", items_jason='sdb', amout=400,
                                                               name='hridoy', email='gh@gmail.com', address="ghg",
                                                               city='cumilla', state='cu', zip_code='3583',
                                                               phone='sgdbj')
        self.order_id.save()
        self.timestamp = date.today()
        self.order = Orders(
            order_id=self.order_id,
            items_jason=self.item_jason
            amount = self.amount
            email = self.email
            address = self.address
            city = self.city
            state = self.state
            zip_code = self.zip_code
            phone = self.phone
        )
        self.order.save()

    def tearDown(self):
        self.order_id.delete()

    def test_read_order(self):
        self.assertEqual(self.order.order_id, self.order_id)
        self.assertEqual(self.order.items_jason, self.items_jason)
        self.assertEqual(self.order.amount, self.amount)
        self.assertEqual(self.order.email, self.email)
        self.assertEqual(self.order.address, self.address)
        self.assertEqual(self.order.city, self.city)
        self.assertEqual(self.order.state, self.state)
        self.assertEqual(self.order.zip_code, self.zip_code)
        self.assertEqual(self.order.phone, self.phone)

    def test_update_order_item_jason(self):
        self.order.items_jason = "new sdg"
        self.order.save()
        self.assertEqual(self.order.items_jason, 'new sdg')

    def test_update_order_amount(self):
        self.order.amount = "450"
        self.order.save()
        self.assertEqual(self.order.amount, '450')

    def test_update_order_name(self):
        self.order.name = "watch"
        self.order.save()
        self.assertEqual(self.order.name, 'watch')

    def test_update_order_email(self):
        self.order.email = "new@gmail.com"
        self.order.save()
        self.assertEqual(self.order.email, 'new@gmail.com')

    def test_update_order_address(self):
        self.order.address = "new 450"
        self.order.save()
        self.assertEqual(self.order.address, 'new 450')

    def test_update_order_city(self):
        self.order.city = "new 450"
        self.order.save()
        self.assertEqual(self.order.amount, '450')

    def test_update_order_state(self):
        self.order.state = "new 450"
        self.order.save()
        self.assertEqual(self.order.state, 'new 450')

    def test_update_order_zip_code(self):
        self.order.zip_code = "new 450"
        self.order.save()
        self.assertEqual(self.order.zip_code, 'new 450')


def test_update_order_phone(self):
    self.order.phone = "new 450"
    self.order.save()
    self.assertEqual(self.order.phone, 'new 450')
