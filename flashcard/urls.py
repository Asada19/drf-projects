from django.urls import path

from .views import CardView, CardDetailView


urlpatterns = [
    path('', CardView.as_view(), name='card-list'),
    path('<int:pk>/', CardDetailView.as_view(), name='card-detail'),
]