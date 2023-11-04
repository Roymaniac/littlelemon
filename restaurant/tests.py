from django.test import TestCase


class TestViews(TestCase):

    def test_get_home_page(self):
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "index.html")

    def test_get_about_page(self):
        page = self.client.get("/about/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "about.html")

    def test_get_book_page(self):
        page = self.client.get("/book/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "book.html")

    def test_get_reservations_page(self):
        page = self.client.get("/reservations/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "bookings.html")

    def test_get_menu_page(self):
        page = self.client.get("/menu/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "menu.html")
