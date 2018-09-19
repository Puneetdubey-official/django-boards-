from django.core.urlresolvers import reverse
from django.test import TestCase


class HomeTests(TestCase):
	def test_home_view_satuts_code(self):
		url = reverse('home')

		response = self.client.get(url)
		self.assertEquals(response.satuts_code, 200)
