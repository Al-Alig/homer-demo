from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from entity.models import Entity, Order, EntityImages
import re


class TestEntityViews(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        self.client.login(username='temporary', password='temporary')

    def test_booking_view(self):
        entity = Entity.objects.create(name='Test Entity', type='1', description='Test Description',
                                       price=100, country='Test Country', city='Test City', address='Test Address',
                                       user=self.user)
        response = self.client.post(reverse('booking', args=[entity.id]), {'FormStart': timezone.now(),
                                                                           'FormEnd': timezone.now()})
        self.assertEqual(response.status_code, 302)

        order_exists = Order.objects.filter(entity=entity.id).exists()
        self.assertTrue(order_exists)

    def test_history_view(self):
        entity = Entity.objects.create(name='Test Entity', type='1', description='Test Description',
                                       price=100, country='Test Country', city='Test City', address='Test Address',
                                       user=self.user)
        order = Order.objects.create(user=self.user, entity=entity, start_date=timezone.now(),
                                     close_date=timezone.now())
        response = self.client.post(reverse('history', args=[entity.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(order, response.context['history'])

    def test_create_application_view(self):
        response = self.client.post(reverse('create_application'), {'formName': 'Test Entity',
                                                                    'formType': '1',
                                                                    'formDescription': 'Test Description',
                                                                    'formPrice': 100,
                                                                    'formCountry': 'Test Country',
                                                                    'formCity': 'Test City',
                                                                    'formAddress': 'Test Address'})
        self.assertEqual(response.status_code, 302)

        entity_exists = Entity.objects.filter(name='Test Entity').exists()
        self.assertTrue(entity_exists)

    def test_entity_detail_view(self):
        entity = Entity.objects.create(name='Test Entity', type='1', description='Test Description',
                                       price=100, country='Test Country', city='Test City', address='Test Address',
                                       user=self.user)
        response = self.client.post(reverse('entity_detail', args=[entity.id]), {'startBook': timezone.now(),
                                                                                  'endBook': timezone.now()})
        self.assertEqual(response.status_code, 302)

        order_exists = Order.objects.filter(entity=entity.id).exists()
        self.assertTrue(order_exists)

    def test_entity_detail_view_invalid_date(self):
        entity = Entity.objects.create(name='Test Entity', type='1', description='Test Description',
                                       price=100, country='Test Country', city='Test City', address='Test Address',
                                       user=self.user)
        response = self.client.post(reverse('entity_detail', args=[entity.id]), {'startBook': timezone.now(),
                                                                                  'endBook': timezone.now()})
        self.assertEqual(response.status_code, 302)

        order_exists = Order.objects.filter(entity=entity.id).exists()
        self.assertFalse(order_exists)


class TestUserViews(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary', phone='+79993235678')

    def test_edit_profile_phone_number(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get(reverse('edit_profile'), follow=True)
        phone_field = response.context['phone']
        pattern = ("^\\+?\\d{1,4}?[-.\\s]?\\(?\\d{1,3}?\\)?[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,4}[-.\\s]?\\d{1,9}$")
        self.assertRegex(phone_field, pattern)
