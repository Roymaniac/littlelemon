from django.test import TestCase
from restaurant.models import Menu, Booking


class MenuTest(TestCase):
    def test_menu_item_creation(self):
        menu = Menu.objects.create(
            name="Grill Beef", price="200", menu_item_description="Grill beef with cheese")
        self.assertEqual(str(menu), menu.name)
        self.assertEqual(str(menu), menu.price)
        self.assertEqual(str(menu), menu.menu_item_description)

    def test_menu_item_status_code(self):
        response = self.client.get('/menu/')
        self.assertEqual(response.status_code, 200)


class BookingTest(TestCase):
    def test_get_booking(self):
        booking = Booking(first_name="John",
                          reservation_date="2020-01-01", reservation_slot="10")
        self.assertEqual(str(booking), booking.first_name)
        self.assertEqual(str(booking), booking.reservation_date)
        self.assertEqual(str(booking), booking.reservation_slot)

    def test_booking_status_code(self):
        response = self.client.get('/booking/')
        self.assertEqual(response.status_code, 200)
