from django.urls import path

from .views import ToDoListView, ToDoListItemView, ToDoListItemDetailView, ToDoListDetailView

urlpatterns = [
    path('list/', ToDoListView.as_view(), name='todo-lists'),
    path('<int:pk>/', ToDoListDetailView.as_view(), name='todo-list-detail'),
    path('<int:pk>/add-item', ToDoListItemView.as_view(), name='todo-item-create'),
    path('item/<int:pk>/', ToDoListItemDetailView.as_view(), name='todo-item-detail'),
]
