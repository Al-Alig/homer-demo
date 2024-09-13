from django.contrib.auth import get_user_model
from django.test import TestCase


class TestUrls(TestCase):
    def setUp(self):
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')

    def test_index(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_add_real_estate(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, 302)

    def test_entity_number_imagined(self):
        response = self.client.get('/entity/100000/')
        self.assertEqual(response.status_code, 404)

    def test_entity_number_existing(self):
        response = self.client.get('/entity/7')
        self.assertEqual(response.status_code, 301)
        self.assertEqual(response.url, '/entity/7/')

    def test_signup(self):
        response = self.client.get('/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login(self):
        response = self.client.post('/login/', {"username": 'temporary', 'password': 'temporary'})
        self.assertEqual(response.status_code, 302)

    def test_logout(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.post('/logout/')
        self.assertEqual(response.status_code, 302)

    def test_profile(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_edit_profile(self):
        self.client.login(username='temporary', password='temporary')
        response = self.client.get('/profile/edit/')
        self.assertEqual(response.status_code, 200)
