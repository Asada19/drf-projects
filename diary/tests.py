from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from django.urls import reverse
import time
from .models import Entry


def get_object():
    return Entry.objects.last()


response_time = 0.03


class EntryTestCase(TestCase):
    def setUp(self):
        Entry(title='Example', content='example').save()
        User(username='example', email='example@gmail.com', password='example').save()
        user = User.objects.last()
        user.is_staff = True
        user.is_admin = True
        user.save()

    def test_entries_get(self):
        user = User.objects.last()
        self.client.force_login(user)

        start_time = time.time()
        response = self.client.get(reverse('entry-list'), format='json')
        end_time = time.time()

        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_entries_get_by_pk(self):
        user = User.objects.last()
        self.client.force_login(user)
        start_time = time.time()
        response = self.client.get(reverse('entry-detail', kwargs={'pk': get_object().pk}), format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_entries_post(self):
        data = {
            'title': 'Sample 2',
            'content': 'Description 2'
        }
        user = User.objects.last()
        self.client.force_login(user)

        start_time = time.time()
        response = self.client.post(reverse('entry-list'), data, format='json')
        end_time = time.time()

        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_entry_update(self):
        user = User.objects.last()
        self.client.force_login(user)

        data = {
            'title': 'Sample 2 Upd',
            'content': 'Description 2 Upd',
        }
        start_time = time.time()
        response = self.client.put(reverse('entry-detail', kwargs={'pk': get_object().pk}),
                                   data, format='json', content_type='application/json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_entry_delete(self):
        user = User.objects.last()
        self.client.force_login(user)
        start_time = time.time()
        response = self.client.delete(reverse('entry-detail', kwargs={'pk': get_object().pk}), format='json',
                                      content_type='application/json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
