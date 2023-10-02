from django.test import SimpleTestCase,TestCase
from django.urls import reverse

class HomepageTests(SimpleTestCase):
    def test_url_exists_at_exact_location(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
    def test_homepage(self):
        response = self.client.get(reverse("BookDonations:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "BookDonations/index.html")
        self.assertContains(response=response, text= "<p>Books given out</p>")

