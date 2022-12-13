import time

from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from portfolio_app.models import Category, Post, Comment

# Create your tests here.

User = get_user_model()
response_time = 0.05
client = RequestsClient()

def get_post():
    return Post.objects.last()


class CategoryTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Category(name='Test1').save()

    def test_get_board(self):
        start_time = time.time()
        response = self.client.get(reverse('category_list'), format='formdata')
        end_time = time.time()
        self.assertLess(end_time-start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_board(self):
        data = {'name': 'Example'}
        start_time = time.time()
        response = self.client.post(reverse('category_list'), data, format='multipart')
        end_time = time.time()
        self.assertLess(end_time-start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 2)

    def test_update_board(self):
        data = {'name': 'Updated name'}
        start_time = time.time()
        response = self.client.patch(reverse('category_detail', kwargs={'pk': 1}), data, format='multipart')
        end_time = time.time()
        self.assertLess(end_time-start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_board(self):
        start_time = time.time()
        response = self.client.delete(reverse('category_detail', kwargs={'pk': 1}))
        end_time = time.time()
        self.assertLess(end_time-start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class PostTestCase(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Category(name='Test1').save()
        Post(title='Example', body='example text')

    def test_get_post(self):
        start_time = time.time()
        response = self.client.get(reverse('post_detail', kwargs={'pk': 1}))
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        data = {'title': 'Updated name', 'body': 'updated body'}
        start_time = time.time()
        response = self.client.patch(reverse('post_detail', kwargs={'pk': 1}), data, format='multipart')
        end_time = time.time()
        self.assertLess(end_time-start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        start_time = time.time()
        response = self.client.delete(reverse('post_detail', kwargs={'pk': 1}))
        end_time = time.time()
        self.assertLess(end_time-start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class CommentTest(APITestCase):
    def setUp(self):
        Category(name='Sample').save()
        Post(title='Sample Post', body='Lorem Ipsum').save()
        Comment(author='Unknown', body='Lorem Ipsum', post=get_post()).save()

    def test_comment_post(self):
        post_pk = get_post().pk
        data = {'author': 'Example', 'body': 'example', 'post': post_pk}
        start_time = time.time()
        response = self.client.post(reverse('add_comment', kwargs={'post_id': 1}), data, format='json',
                                    content_type='application/json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
