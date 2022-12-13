from django.urls import path

from .views import ToDoListView, ToDoListItemView, ToDoListItemDetailView, ToDoListDetailView

urlpatterns = [
    path('to-do/', ToDoListView.as_view(), name='todo-lists'),
    path('to-do/<int:pk>/', ToDoListDetailView.as_view(), name='todo-list-detail'),
    path('to-do/<int:pk>/item', ToDoListItemView.as_view(), name='todo-item-create'),
    path('to-do/<int:pk>/', ToDoListItemDetailView.as_view(), name='todo-item-detail'),
]
