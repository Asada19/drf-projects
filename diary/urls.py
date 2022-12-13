from django.urls import path

from .views import EntryListAPIView, EntryDetailView

urlpatterns = [
    path('', EntryListAPIView.as_view(), name='entry-list'),
    path('<int:pk>/', EntryDetailView.as_view(), name='entry-detail'),
]
