from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from .models import Episode
from django.urls import reverse
import time

response_time = 0.03


class EpisodeTestCase(TestCase):
    def setUpTestData(self):
        Episode(title='Example',
                description='example',
                pub_date=timezone.now(),
                link='example',
                image='example',
                podcast_name='example',
                guid='example').save()

    def test_episode_get(self):
        start_time = time.time()
        response = self.client.get(reverse('episodes'), format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
