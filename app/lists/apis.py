from rest_framework import generics, permissions

from .models import List
from .serializers import ListSerializer

__all__ = (
    'ListListCreateAPIView',
    'ListRetrieveUpdateDestroyAPIView',
)


class ListListCreateAPIView(generics.ListCreateAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )


class ListRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
