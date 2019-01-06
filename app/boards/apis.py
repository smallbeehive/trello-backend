from rest_framework import generics, permissions

from .models import Board
from .serializers import BoardSerializer

__all__ = (
    'BoardListCreateAPIView',
    'BoardRetrieveUpdateDestroyAPIView',
)


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BoardRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )
