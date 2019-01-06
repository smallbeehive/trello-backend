from rest_framework import generics, permissions

from boards.models import Board
from boards.serializers import BoardSerializer

__all__ = (
    'BoardListCreateAPIView',
)


class BoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    permission_classes = (
        permissions.IsAuthenticated,
    )

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
