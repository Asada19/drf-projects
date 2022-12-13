from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Card


class CardTestCase(APITestCase):

    def setUp(self):
        card = Card(question="example", answer="example", box=5)
        card.save()

    def test_get_card_list(self):
        response = self.client.get(reverse("card-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_card_create(self):
        response = self.client.post(reverse("cards-list"), {"question": "Question 1", "answer": "Answer 1", "box": 4})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_card_view(self):
        card = Card.objects.get(question="example")
        response = self.client.get(reverse("card-detail", kwargs={"pk": card.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_card_update(self):
        card = Card.objects.get(question="example")
        response = self.client.put(reverse("card-detail", kwargs={"pk": card.id}),
                                   {"question": "Q 2",
                                    "answer": "A 2",
                                    "box": 3})
        self.assertEqual(response.status_code, status.HTTP_200_OK)


