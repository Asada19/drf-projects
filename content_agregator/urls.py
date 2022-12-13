from django.urls import path

from .views import EpisodeListAPIView

urlpatterns = [
    path('', EpisodeListAPIView.as_view(), name='episodes'),
]