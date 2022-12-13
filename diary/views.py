from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Entry
from .serializers import EntrySerializer


class EntryListAPIView(ListCreateAPIView):
    model = Entry
    serializer_class = EntrySerializer
    parser_classes = (MultiPartParser, FormParser)

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset


class EntryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Entry.objects.all()
    model = Entry
    serializer_class = EntrySerializer


