from rest_framework.test import APITestCase
from rest_framework import status
from restaurant.models import Menu, Booking
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from restaurant.views import MenuViewSet, BookingViewSet


class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword')
        self.token = Token.objects.get_or_create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

        self.menu_data = {"name": "Grill Beef", "price": "200",
                          "menu_item_description": "Grill beef with cheese"}
        self.menu = Menu.objects.create(**self.menu_data)

    def test_create_menu(self):
        response = self.client.post('/menu/', self.menu_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Menu.objects.count(), 3)

    def test_get_menu(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.count(), 3)

    def test_update_menu(self):
        response = self.client.put('/menu/1/', self.menu_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Menu.objects.count(), 3)

    def test_delete_menu(self):
        response = self.client.delete('/menu/1/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Menu.objects.count(), 2)
