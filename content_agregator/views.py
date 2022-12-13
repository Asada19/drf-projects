from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView

from .models import Episode
from .serializers import EpisodeSerializer


class EpisodeListAPIView(ListAPIView):
    queryset = Episode.objects.all().order_by("-pub_date")[:20]
    serializer_class = EpisodeSerializer
    pagination_class = PageNumberPagination

