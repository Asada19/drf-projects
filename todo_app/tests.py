from django.test import TestCase
from django.utils import timezone
from rest_framework import status
from django.urls import reverse
import time

from .models import ToDoList, ToDoItem


def get_todolist():
    return ToDoList.objects.all().last()


def get_todoitem():
    return ToDoItem.objects.all().last()


response_time = 0.05


class ToDoTestCase(TestCase):
    def setUpTestData(self):
        ToDoList(title='Example').save()

    def test_get_todo_list(self):
        start_time = time.time()
        response = self.client.get(reverse('api-todo-lists'), format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todo_lists(self):
        data = {
            'title': 'Sample 2'
        }
        start_time = time.time()
        response = self.client.post(reverse('api-todo-lists'), data, format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_todo_list(self):
        start_time = time.time()
        todolist_pk = get_todolist().pk
        response = self.client.get(reverse('api-todolist-detail', kwargs={'pk': todolist_pk}), format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_todo_list(self):
        start_time = time.time()
        todolist_pk = get_todolist().pk
        response = self.client.delete(reverse('api-todolist-detail', kwargs={'pk': todolist_pk}), format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class ToDoItemTest(TestCase):

    def setUp(self):
        ToDoList(title='Example').save()
        ToDoItem(title='Exmaple Title', description='Example desc',
                 due_date=timezone.now(), todo_list=get_todolist()).save()

    def test_item_create(self):
        data = {
            'title': 'Example To Do 2',
            'description': 'Example description 2',
        }
        start_time = time.time()
        response = self.client.post(reverse('todo-item-create', kwargs={'pk': get_todolist().pk}), data, format='json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_update(self):
        data = {
            'title': 'Sample To Do 2 Upd',
            'description': 'Lorem Ipsum 2 Upd',
        }
        start_time = time.time()
        response = self.client.put(reverse('todo-item-detail', kwargs={'pk': get_todoitem().pk}), data, format='json', content_type='application/json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_item_delete(self):
        start_time = time.time()
        response = self.client.delete(reverse('todo-item-detail', kwargs={'pk': get_todoitem().pk}),
                                   format='json', content_type='application/json')
        end_time = time.time()
        self.assertLess(end_time - start_time, response_time)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
